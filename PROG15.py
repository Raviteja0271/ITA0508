import cv2
import numpy as np

# Read the image
image = cv2.imread("your_image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray = np.float32(gray)

# Apply Harris Corner detection
corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate corner image to enhance the corners
corners = cv2.dilate(corners, None)

# Threshold to mark the corners in red
image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Display the result
cv2.imshow("Corners", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
