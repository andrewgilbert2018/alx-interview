#!/usr/bin/python3
"""
Script for rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Function that rotates the matrix 90 degrees
    """
    ft_matrix = matrix[:]
    matrix.clear()
    rotated_matrix = list(map(lambda x: list(x), zip(*ft_matrix[::-1])))
    matrix.extend(rotated_matrix)
