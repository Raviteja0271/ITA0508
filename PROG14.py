import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("your_image.jpg")  # Replace with your image path

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Get the image dimensions (height, width)
    rows, cols = image.shape[:2]

    # Define the four source points (in the original image)
    src_points = np.float32([[100, 100], [400, 100], [100, 400], [400, 400]])

    # Define the four destination points (where you want to map the source points)
    dst_points = np.float32([[50, 150], [450, 100], [100, 450], [450, 450]])

    # Get the perspective transformation matrix
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    # Apply the perspective transformation
    transformed_image = cv2.warpPerspective(image, M, (cols, rows))

    # Convert BGR to RGB for displaying with matplotlib
    transformed_image_rgb = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)

    # Display the original and transformed images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(transformed_image_rgb)
    plt.title("Perspective Transformed Image")
