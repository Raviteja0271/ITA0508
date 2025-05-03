import cv2

# Load the image
image = cv2.imread("your_image.jpg")

# Define the Region of Interest (ROI)
roi = image[50:200, 100:300].copy()  # Make a copy to ensure proper assignment

# Get the size of the ROI
roi_height, roi_width, _ = roi.shape

# Ensure destination coordinates are valid
dest_y, dest_x = 250, 300  # Define the destination start point
if dest_y + roi_height <= image.shape[0] and dest_x + roi_width <= image.shape[1]:
    image[dest_y:dest_y+roi_height, dest_x:dest_x+roi_width] = roi  # Assign ROI
else:
    print("Error: Destination coordinates exceed image dimensions.")

# Display the result
cv2.imshow("Modified Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
