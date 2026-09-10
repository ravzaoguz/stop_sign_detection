import cv2 as cv
import numpy as np

images = ["sign_1.jpg", "sign_2.jpeg", "sign_3.jpg"]

for file in images:
    image = cv.imread(file)

    if image is None:
        print(f"Error: could not read {file}")
        continue

    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv.inRange(hsv_image, lower_red1, upper_red1)

    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv.inRange(hsv_image, lower_red2, upper_red2)

    red_mask = cv.bitwise_or(mask1, mask2)

    contours, hierarchies = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)

        if cv.contourArea(largest_contour) > 500:
            x, y, w, h = cv.boundingRect(largest_contour)

            center_x = x + w // 2
            center_y = y + h // 2

            print(f"{file} -> center pixel : X={center_x}, Y={center_y}")

            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv.circle(image, (center_x, center_y), 5, (255, 0, 0), -1)

            output = f"output_{file}"
            cv.imwrite(output, image)

            cv.imshow("Stop Sign Detection", image)
            cv.waitKey(0)

cv.destroyAllWindows()