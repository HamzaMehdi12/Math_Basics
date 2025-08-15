## Linear Algebra
Here we implement the basics of Mathematics and functions that would be used in Machine Learning, and in general, in daily-life case

### Results

### Matrix A (5x5)

|       | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
|-------|-------|-------|-------|-------|-------|
| Row 1 | 0     | 2     | 4     | 6     | 8     |
| Row 2 | 2     | 4     | 6     | 8     | 10    |
| Row 3 | 4     | 6     | 8     | 10    | 12    |
| Row 4 | 6     | 8     | 10    | 12    | 14    |
| Row 5 | 8     | 10    | 12    | 14    | 16    |

### Matrix B (5x5)

|       | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
|-------|-------|-------|-------|-------|-------|
| Row 1 | 0     | 3     | 6     | 9     | 12    |
| Row 2 | 3     | 6     | 9     | 12    | 15    |
| Row 3 | 6     | 9     | 12    | 15    | 18    |
| Row 4 | 9     | 12    | 15    | 18    | 21    |
| Row 5 | 12    | 15    | 18    | 21    | 24    |

---

### Matrix Multiplication Result (A × B)

|       | Result |
|-------|--------|
| Row 1 | 180    |
| Row 2 | 330    |
| Row 3 | 540    |
| Row 4 | 810    |
| Row 5 | 1140   |

---

### Matrix Inverse Example

### Original Matrix for Inverse (2x2)

|       | Col 1 | Col 2 |
|-------|-------|-------|
| Row 1 | 4     | 4     |
| Row 2 | 4     | 8     |

### Completed Inverse

|       | Col 1 | Col 2 |
|-------|-------|-------|
| Row 1 | 4     | 4     |
| Row 2 | 4     | 8     |

---

### Eigenvalues and Eigenvectors

- Matrix: 

|       | Col 1 | Col 2 |
|-------|-------|-------|
| Row 1 | 4     | 4     |
| Row 2 | 4     | 8     |

- Eigenvalues: **a = -12, b = -8**  
- Reduced Form: 

|       | Col 1 | Col 2 |
|-------|-------|-------|
| Row 1 | 1.0   | 0.0   |
| Row 2 | 0.0   | 1.0   |

---

### Singular Value Decomposition (SVD)

- Matrix for SVD:

|       | Col 1 | Col 2 |
|-------|-------|-------|
| Row 1 | 1.0   | 0.0   |
| Row 2 | 0.0   | 1.0   |


## Probaility and Statistics
We develop a statistical pipeline without the aid of any library. We received the following results:


### Dataset Overview

Array A passed with values (10x10), rows: 10, cols: 10:

|       | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 | Col 9 | Col 10 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|
| Row 1 | 0     | 1     | 4     | 3     | 8     | 5     | 12    | 7     | 16    | 9      |
| Row 2 | 10    | 6     | 14    | 8     | 18    | 10    | 22    | 12    | 26    | 14     |
| Row 3 | ...   | ...   | ...   | ...   | ...   | ...   | ...   | ...   | ...   | ...    |
| Row 10| ...   | ...   | ...   | ...   | ...   | ...   | ...   | ...   | ...   | ...    |

---

### Statistics Computed

| Metric            | Value  | Formula / Description                                     |
|------------------|--------|-----------------------------------------------------------|
| Arithmetic Mean   | **13.25** | \(\text{Mean} = \frac{\text{Sum of all elements}}{\text{Number of elements}}\) |
| Variance          | **54.69** | \(\text{Variance} = \frac{\sum (x_i - \bar{x})^2}{n}\) |
| Distribution PDF  | 20 elements | Values of probability density function for dataset elements |
| CDF               | 20 elements | Cumulative distribution function from the PDF          |

---
### Results
Below are the results of the processed data in ***PDF*** and ***CDF***

<img width="1920" height="967" alt="pdf_normal_for_20x20mat" src="https://github.com/user-attachments/assets/65b44387-a631-4dfd-969c-c312e26d481c" />

<img width="1920" height="967" alt="cdf_normal_for_20x20mat" src="https://github.com/user-attachments/assets/7c18e351-9e91-48b4-bb49-2eb903639652" />














