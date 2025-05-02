import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("your_image.jpg")  # Replace with your image path

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Define the points in the original image
    rows, cols = image.shape[:2]

    # Example: Specify three points in the original image (source points)
    src_points = np.float32([[50, 50], [200, 50], [50, 200]])

    # Example: Specify three corresponding points in the transformed image (destination points)
    dst_points = np.float32([[10, 100], [200, 50], [100, 250]])

    # Get the affine transformation matrix
    M = cv2.getAffineTransform(src_points, dst_points)

    # Apply the affine transformation
    transformed_image = cv2.warpAffine(image, M, (cols, rows))

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
    plt.title("Affine Transformed Image")
    plt.axis("off")

    plt.show()
