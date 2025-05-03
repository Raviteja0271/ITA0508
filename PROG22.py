import cv2
import numpy as np

# Load the image
image = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Apply the Closing operation (dilation followed by erosion)
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the result
cv2.imshow("Original Image", image)
cv2.imshow("Closed Image", closed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
