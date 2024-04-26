#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
    - n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    - list of lists: A list of lists representing Pascal's triangle.
      Each inner list represents a row in the triangle, with the
      first element being the first row, the second element being
      the second row, and so on. Each row contains the corresponding
      coefficients of the binomial expansion of (a + b)^n.

    Raises:
    - None.

    Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> pascal_triangle(0)
    []
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
