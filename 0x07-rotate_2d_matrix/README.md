# Rotate 2D Matrix

## Introduction
This project implements an algorithm to rotate an n x n 2D matrix by 90 degrees clockwise in Python. The rotation is done in place, meaning the original matrix is modified rather than creating a new one.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the project folder, is mandatory
- Code should use the pycodestyle style (version 2.8.0)
- No external modules should be imported
- All modules and functions must be documented
- All files must be executable

## Usage
To rotate a 2D matrix, import the `rotate_2d_matrix` function from the `0-rotate_2d_matrix.py` file and pass the matrix as an argument. The function will rotate the matrix in place without returning anything.

Example usage:
```python
from 0-rotate_2d_matrix import rotate_2d_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
