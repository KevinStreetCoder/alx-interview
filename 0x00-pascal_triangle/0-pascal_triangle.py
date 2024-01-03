def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    - n: Integer representing the number of rows to generate.

    Returns:
    - List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle

# Example usage
if __name__ == "__main__":
    result = pascal_triangle(5)
    for row in result:
        print(row)
