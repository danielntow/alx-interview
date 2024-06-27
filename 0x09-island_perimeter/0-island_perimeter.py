#!/usr/bin/python3
"""
island perimeter module
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 1 represents land 
        and 0 represents water.

    Returns:
        int: Perimeter of the island.

    Raises:
        ValueError: If grid is empty or not rectangular.

    Example:
        >>> island_perimeter([[0, 1, 0, 0],
        ...                   [1, 1, 1, 0],
        ...                   [0, 1, 0, 0],
        ...                   [1, 1, 0, 0]])
        16
    """
    if not grid or not all(isinstance(row, list) for row in grid):
        raise ValueError("Grid should be a non-empty list of lists.")
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with maximum perimeter for each land cell
                # Check adjacent cells (left, right, up, down) and reduce 
                # perimeter if adjacent cell is land
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    
    return perimeter
