import numpy as np
import matplotlib.pyplot as plt
import sys

# Check if the input and iutput file paths are given in the CLI.
if len(sys.argv) < 3:
    print("Error:Missing Arguments")
    print("Usage:\npython main.py <input_img_file_path> <output_img_file_path>")
    sys.exit(1)

# Assign the paths to variables
input_path = sys.argv[1]
output_path = sys.argv[2]

# Check if the input file exists by trying to read it
try:
   img_array = plt.imread(input_path)
except FileNotFoundError:
    print("Error: Missing Input Image File")
    print("Make sure the input image path is specified correctly")
    sys.exit(1)

# Each element is a weight on the RGB values respectively
grayscale_weights = np.array([0.299, 0.587, 0.114])

# Get the dot product of the weights and pixel values, round up elements to the nearest integer and convert array elements to an unsigned 8 byte integer
grayscale_image_arr = np.rint(np.dot(img_array,grayscale_weights)).astype("u8")

# Save the image in raw format
plt.imsave(output_path, grayscale_image_arr, cmap="gray")
print("Image succesfully converted to grayscale")
print(f"Grayscale image saved to '{output_path}'")