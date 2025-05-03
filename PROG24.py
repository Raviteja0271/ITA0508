import cv2
import numpy as np

# Load the image
image = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel)
kernel = np.ones((15, 15), np.uint8)  # 15x15 kernel for processing

# Apply Black-Hat transformation
black_hat_image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Display the result
cv2.imshow("Original Image", image)
cv2.imshow("Black-Hat Image", black_hat_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
