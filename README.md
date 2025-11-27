# **Image to Grayscale Converter**

A simple, efficient Python script that converts RGB images to grayscale using the luminosity method.

## **Description**

This command-line tool takes an input image file, processes its pixel data using numpy matrix operations, and outputs a grayscale version. It utilizes standard colorimetric weights (Rec. 601\) for the conversion to ensure the resulting grayscale image matches human brightness perception.

## **Features**

* **Command Line Interface:** Easy to run from a terminal with arguments for input and output paths.  
* **Weighted Conversion:** Uses the formula Y \= 0.299R \+ 0.587G \+ 0.114B for natural-looking results.  
* **Error Handling:** Checks for missing arguments and invalid file paths.

## **Prerequisites**

You need Python installed on your system along with the following libraries:

* numpy  
* matplotlib

## **Installation**

1. Clone this repository or save the script as main.py.  
2. Install the required packages using pip:

pip install numpy matplotlib

## **Usage**

Run the script from your terminal using the following format:

python main.py \<input\_img\_file\_path\> \<output\_img\_file\_path\>

### **Arguments**

* \<input\_img\_file\_path\>: The path to the image you want to convert (e.g., photo.jpg).  
* \<output\_img\_file\_path\>: The path (including filename) where the result should be saved (e.g., photo\_gray.png).

### **Example**

python main.py my\_vacation.jpg grayscale\_vacation.png

## **How It Works**

1. **Load:** The image is loaded into a NumPy array.  
2. **Calculate:** The script calculates the dot product of the RGB values with the weights \[0.299, 0.587, 0.114\]. This specific weighting accounts for the fact that human eyes are more sensitive to green light, less to red, and least to blue.  
3. **Save:** The resulting array is cast to unsigned 8-bit integers and saved using the 'gray' colormap.