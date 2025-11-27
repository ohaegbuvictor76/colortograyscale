import numpy as np
import matplotlib.pyplot as plt

path = "input.jpeg"
img_array = plt.imread(path)
grayscale_weights = np.array([0.299, 0.587, 0.114])

# Get the dot product of the weights and pixel values, round up elements to the nearest integer and covert elements to an unsigned 8 byte integer
grayscale_image_arr = np.rint(np.dot(img_array,grayscale_weights)).astype("u8")

# Covert the array to an image
plt.imshow(grayscale_image_arr, cmap="gray")
plt.axis("off") # Remove the axes

# Save the image in raw format and show
plt.imsave("output.jpeg", grayscale_image_arr, cmap="gray")
plt.show()