import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the image
image = cv2.imread("your_image.jpg")  # Replace with the correct path to your image

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Step 2: Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply dilation
    # Define a kernel (a simple 3x3 matrix of ones)
    kernel = np.ones((3, 3), np.uint8)

    # Perform dilation
    dilated_image = cv2.dilate(gray_image, kernel, iterations=1)

    # Step 4: Display the original and dilated images using matplotlib
    plt.figure(figsize=(10,5))

    # Show original image
    plt.subplot(1, 2, 1)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Original Grayscale Image")
    plt.axis("off")

    # Show dilated image
    plt.subplot(1, 2, 2)
    plt.imshow(dilated_image, cmap="gray")
    plt.title("Dilated Image")
    plt.axis("off")

    # Display the images
    plt.show()
