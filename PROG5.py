import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found or failed to load.")
        return
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    r, g, b = cv2.split(img_rgb)

    plt.figure(figsize=(10, 6))
    plt.subplot(1, 3, 1)
    plt.hist(r.ravel(), bins=256, color='red', alpha=0.7)
    plt.title('Red Channel Histogram')
    plt.subplot(1, 3, 2)
    plt.hist(g.ravel(), bins=256, color='green', alpha=0.7)
    plt.title('Green Channel Histogram')
    plt.subplot(1, 3, 3)
    plt.hist(b.ravel(), bins=256, color='blue', alpha=0.7)
    plt.title('Blue Channel Histogram')

    plt.tight_layout()
    plt.show()

# Example usage
analyze_histogram("your_image.jpg")
