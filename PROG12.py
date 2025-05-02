import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("your_image.jpg")  # Replace with your image file path

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Rotate the image by 270 degrees (3 * 90 degrees clockwise)
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_90_CLOCKWISE)
    rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_90_CLOCKWISE)

    # Convert BGR to RGB for displaying with matplotlib
    rotated_image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

    # Display the original and rotated images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(rotated_image_rgb)
    plt.title("270-degree Rotated Image")
    plt.axis("off")

    plt.show()
