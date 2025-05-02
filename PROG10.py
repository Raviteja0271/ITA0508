import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("your_image.jpg")  # Replace with the correct path to your image

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Rotate the image 90 degrees clockwise
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Display the original and rotated images using matplotlib
    plt.figure(figsize=(10,5))

    # Show original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    # Show rotated image
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
    plt.title("Rotated Image (90 degrees)")
    plt.axis("off")

    # Display the images
    plt.show()
