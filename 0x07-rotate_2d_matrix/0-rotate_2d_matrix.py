#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix by 90 degrees clockwise in-place.

    Args:
        matrix: A 2D list representing the matrix to be rotated.

    Raises:
        ValueError: If the matrix is not square.
    """

    n = len(matrix)

    # Check if the matrix is square (necessary for correct rotation)
    if n != len(matrix[0]):
        raise ValueError("Matrix must be square to rotate in-place.")

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to achieve 90-degree clockwise rotation
    for i in range(n):
        matrix[i] = matrix[i][::-1]
