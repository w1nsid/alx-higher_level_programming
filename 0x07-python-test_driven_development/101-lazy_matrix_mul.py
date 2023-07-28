#!/usr/bin/python3
"""Module to define a matrix multiplication function using NumPy library."""
import numpy as np


def lazy_matrix_mul(matrix_1, matrix_2):
    """Return the product of two matrices.

    Args:
        matrix_1 (list of lists of ints/floats): The first input matrix.
        matrix_2 (list of lists of ints/floats): The second input matrix.
    """

    return (np.matmul(matrix_1, matrix_2))
