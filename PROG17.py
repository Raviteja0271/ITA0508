import cv2
import numpy as np

# Load the original image
image = cv2.imread("your_image.jpg")

# Define watermark text
watermark_text = "Confidential"

# Choose font, size, and position
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 3
text_position = (50, 50)  # Adjust based on your image size

# Get text size
text_size = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)[0]

# Create a transparent layer
overlay = image.copy()

# Add text with opacity
cv2.putText(overlay, watermark_text, text_position, font, font_scale, (255, 255, 255), font_thickness)

# Blend the original image and overlay to make watermark semi-transparent
alpha = 0.5  # Adjust transparency level (0 to 1)
watermarked_image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

# Save and display the result
cv2.imshow("Watermarked Image", watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
