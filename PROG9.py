import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("your_image.jpg")  # Replace with the correct path to your image

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Resize to a smaller size (50% of the original size)
    small_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    # Resize to a larger size (200% of the original size)
    large_image = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

    # Display the original, small, and large images using matplotlib
    plt.figure(figsize=(15,5))

    # Show original image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    # Show small image
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(small_image, cv2.COLOR_BGR2RGB))
    plt.title("Smaller Image")
    plt.axis("off")

    # Show large image
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(large_image, cv2.COLOR_BGR2RGB))
    plt.title("Larger Image")
    plt.axis("off")

    # Display the images
    plt.show()
