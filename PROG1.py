import cv2

# Load the image
image = cv2.imread("your_image.jpg")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save or display the grayscale image
cv2.imwrite("gray_image.jpg", gray_image)  # To save
# or
cv2.imshow("Grayscale Image", gray_image)  # To display
cv2.waitKey(0)
cv2.destroyAllWindows()
