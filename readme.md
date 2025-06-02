# 🌿 Barnsley Fern Generator

This project generates a beautiful leaf-like fractal known as the **Barnsley Fern** using an Iterative Function System (IFS). The fern is created by iteratively applying a set of affine transformations to a point in 2D space, with each transformation chosen randomly based on assigned probabilities. The result is a stunning fractal pattern that resembles a fern leaf.

## 📖 Overview

The Barnsley fern is a fractal named after mathematician Michael Barnsley. It’s a classic example of how simple mathematical rules can generate complex, natural-looking patterns. The fern is created by applying four specific affine transformations to a point, iterating tens of thousands of times, and plotting the resulting points.

### The Formula

Each transformation in the IFS is an **affine transformation** of the form:

\[
\begin{bmatrix}
x_{n+1} \\
y_{n+1}
\end{bmatrix}
=
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\begin{bmatrix}
x_n \\
y_n
\end{bmatrix}
+
\begin{bmatrix}
e \\
f
\end{bmatrix}
\]

- \([x_n, y_n]\): The current point.
- \([x_{n+1}, y_{n+1}]\): The next point after applying the transformation.
- \(\begin{bmatrix} a & b \\ c & d \end{bmatrix}\): A 2x2 matrix that scales, rotates, or shears the point.
- \(\begin{bmatrix} e \\ f \end{bmatrix}\): A 2x1 bias vector that translates the point.

The Barnsley fern uses four transformations, each with a specific probability of being applied:

1. **Stem** (1% probability):
   \[
   \begin{bmatrix}
   0.00 & 0.00 \\
   0.00 & 0.16
   \end{bmatrix}
   \begin{bmatrix}
   x_n \\
   y_n
   \end{bmatrix}
   +
   \begin{bmatrix}
   0.00 \\
   0.00
   \end{bmatrix}
   \]

2. **Smaller leaflets (left)** (7% probability):
   \[
   \begin{bmatrix}
   0.20 & -0.26 \\
   0.23 & 0.22
   \end{bmatrix}
   \begin{bmatrix}
   x_n \\
   y_n
   \end{bmatrix}
   +
   \begin{bmatrix}
   0.00 \\
   1.60
   \end{bmatrix}
   \]

3. **Smaller leaflets (right)** (7% probability):
   \[
   \begin{bmatrix}
   -0.15 & 0.28 \\
   0.26 & 0.24
   \end{bmatrix}
   \begin{bmatrix}
   x_n \\
   y_n
   \end{bmatrix}
   +
   \begin{bmatrix}
   0.00 \\
   0.44
   \end{bmatrix}
   \]

4. **Main leaf structure** (85% probability):
   \[
   \begin{bmatrix}
   0.85 & 0.04 \\
   -0.04 & 0.85
   \end{bmatrix}
   \begin{bmatrix}
   x_n \\
   y_n
   \end{bmatrix}
   +
   \begin{bmatrix}
   0.00 \\
   1.60
   \end{bmatrix}
   \]

### How It Works

1. **Starting Point**: Begin with an initial point, \([x_0, y_0] = [0, 0]\).
2. **Random Selection**: At each iteration, randomly choose one of the four transformations based on their probabilities (0.01, 0.07, 0.07, 0.85).
3. **Apply Transformation**: Use the selected transformation to compute the next point \([x_{n+1}, y_{n+1}]\) using the formula above.
4. **Iterate**: Repeat this process many times (e.g., 100,000 iterations) to generate a large set of points.
5. **Plot**: Plot all the points as a scatter plot to reveal the fern shape.

The high probability of the fourth transformation ensures the main structure of the fern forms, while the other transformations create the stem and smaller leaflets.

## 🛠️ Code Explanation

The Python code uses `numpy` for matrix operations and `matplotlib` for plotting. Here’s a breakdown of the key steps:

- **Define Transformations**: A list of dictionaries stores the 2x2 matrices, bias vectors, and probabilities for the four transformations.
- **Cumulative Probabilities**: Compute cumulative probabilities to efficiently select transformations randomly.
- **Iterative Process**: Loop 100,000 times, each time selecting a transformation, applying it to the current point, and storing the new point.
- **Plotting**: Use `matplotlib` to create a scatter plot of the points, with small green dots to mimic the appearance of a fern.

### Requirements

- Python 3.x
- `numpy` (for matrix operations)
- `matplotlib` (for plotting)

Install the dependencies using:

```bash
pip install numpy matplotlib
```

### Running the Code

1. Save the code in a file, e.g., `barnsley_fern.py`.
2. Run the script:

```bash
python barnsley_fern.py
```

3. A window will display the Barnsley fern plot.

## 📊 Output

The output is a scatter plot of 100,000 points forming a fern-like shape. The plot has:
- **Green points** to resemble a leaf.
- **Equal axes** to maintain the correct proportions.
- A title, "Barnsley Fern (Leaf Shape)," and labeled axes.

The resulting image looks like a natural fern with a stem and leaflets, showcasing the beauty of fractals in mathematics.

## 🎨 Customization

You can tweak the following parameters in the code:
- **Number of Points**: Change `num_points` to generate more or fewer points (more points give a denser fern).
- **Colors**: Modify the `color` parameter in `plt.scatter()` to change the fern’s color.
- **Transformations**: Adjust the matrices, biases, or probabilities to create different fractal patterns.

## 🌟 Why It’s Beautiful

The Barnsley fern demonstrates how simple mathematical rules can create complex, organic shapes. It’s a perfect blend of mathematics and art, showing how nature’s patterns can be modeled with fractals. The iterative process mimics growth, where each point contributes to the overall structure of the fern, resulting in a visually stunning leaf-like form.

---

