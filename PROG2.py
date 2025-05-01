import cv2

image = cv2.imread("your_image.jpg")

blur = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow("Blurred", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
