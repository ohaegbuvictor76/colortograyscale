```markdown
# Colored to Grayscale Converter

A high-performance CLI tool for converting RGB images to grayscale using NumPy vectorization.

## 🚀 Overview
This project is a command-line utility that converts standard image formats (JPG, PNG) into grayscale. Unlike standard looping methods, this tool utilizes **NumPy matrix multiplication** to apply the luminosity method  
(Y = 0.299·R + 0.587·G + 0.114·B)  
across the entire pixel array simultaneously, ensuring O(1) complexity relative to Python interpreter overhead.

## 🛠️ Technologies
* **Python 3.12**
* **NumPy** (Vectorized Linear Algebra)
* **Matplotlib** (Image I/O)
* **Anaconda** (Environment Management)

## 💻 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/oheagbuvictor76/colortograyscale.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd colortograyscale
   ```

3. **Install dependencies:**
   ```bash
   pip install numpy matplotlib
   ```

## 📖 Usage

Run the script from the terminal by specifying the input image path and the desired output path:

```bash
python main.py <input_image_path> <output_image_path>
```

**Example:**
```bash
python main.py input.jpg output_gray.jpg
```

## ⚙️ How It Works

1. **CLI Parsing:** Uses `sys.argv` to accept dynamic file paths from the command line.
2. **Data Loading:** Loads image data into a 3D NumPy array `(Height, Width, 3)`.
3. **Vectorization:** Performs a dot product between the RGB channels and the standard luminosity weights `[0.299, 0.587, 0.114]`.
4. **Optimization:** Implements single-pass file reading and “Fail Fast” error handling for missing files or arguments.
```