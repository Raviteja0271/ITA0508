import cv2

image = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE)

equalized = cv2.equalizeHist(image)

cv2.imshow("Original Image", image)
cv2.imshow("Equalized Image", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
