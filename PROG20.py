import cv2
import numpy as np

# Load the image
image = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display the result
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
