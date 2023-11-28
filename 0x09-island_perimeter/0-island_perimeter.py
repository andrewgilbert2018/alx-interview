#!/usr/bin/python3
"""[Checks for the perimeter in a GRID island]
"""


def search_perimeter(vector, perimeter, actual):
    """Search for the perimeter

    Args:
        vector: row or column to search for perimeter
        perimeter: perimeter accumulator
        actual: actual iteration
    """
    prev_val = actual - 1
    next_val = actual + 1
    if (vector[actual] == 1):
        if (vector[prev_val] == 0 and prev_val >= 0):
            perimeter += 1
        elif (prev_val < 0):
            perimeter += 1
        if next_val >= len(vector):
            perimeter += 1
        elif (vector[next_val] == 0):
            perimeter += 1
    return perimeter


def island_perimeter(grid):
    """[Receives a grid and return the perimeter of land]

    Args:
        grid ([list of list]): map of the island
    """
    perimeter = 0
    if not grid:
        return perimeter
    if not grid[0]:
        return perimeter
    num_col = len(grid[0])
    for row in grid:
        for actual in range(len(row)):
            perimeter = search_perimeter(row, perimeter, actual)
    for i in range(num_col):
        column = [row[i] for row in grid]
        for actual in range(len(column)):
            perimeter = search_perimeter(column, perimeter, actual)
    return(perimeter)
