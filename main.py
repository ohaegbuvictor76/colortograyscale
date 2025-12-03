import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

# Check if the input and iutput file paths are given in the CLI.
if len(sys.argv) < 3:
    print("Usage:\npython main.py <input_img_file_path> <output_img_file_path>\n")
    print("Some arguments were not given in the CLI you can run it again with the above format or use the inputs below.\n")
    input_path = Path(input("What is the file path to the image you want to convert to grayscale: "))
    output_path = Path(input("What do you want to save the grayscale image as (Enter the path with the extension included): "))
else: 
    # Assign the paths to variables
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])



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