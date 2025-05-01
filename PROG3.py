import cv2

image = cv2.imread("your_image.jpg")

edges = cv2.Canny(image, 100, 200)  
cv2.imshow("Canny Edge", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
