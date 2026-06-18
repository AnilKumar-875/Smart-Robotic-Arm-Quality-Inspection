import cv2
import csv
import os

# Create CSV file
file = open("report.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(
    ["Image", "Area", "Status"]
)

# Process all images
for image_file in os.listdir("images"):

    print("\nProcessing:", image_file)

    path = os.path.join(
        "images",
        image_file
    )

    img = cv2.imread(path)

    if img is None:
        print("Could not read image")
        continue

    # Convert to grayscale
    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    # OTSU Threshold
    _, thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Save threshold image
    cv2.imwrite(
        f"{image_file}_thresh.png",
        thresh
    )

    # Find contours
    contours, hierarchy = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    print("Contours =", len(contours))

    # If no contour found
    if len(contours) == 0:

        writer.writerow(
            [image_file, 0, "No Object"]
        )

        print("No Object Detected")
        continue

    # Largest contour
    contour = max(
        contours,
        key=cv2.contourArea
    )

    area = cv2.contourArea(contour)

    # Classification
    if area > 45000:
        status = "Good"
    else:
        status = "Defective"

    # Bounding box
    x, y, w, h = cv2.boundingRect(contour)

    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        img,
        status,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Save result image
    cv2.imwrite(
        f"result_{image_file}",
        img
    )

    print("Area =", area)
    print("Status =", status)

    writer.writerow(
        [image_file, area, status]
    )

file.close()

print("\nInspection Complete")
print("Report saved as report.csv")