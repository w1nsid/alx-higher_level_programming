#!/usr/bin/python3
"""Module to define a matrix multiplication operation."""


def matrix_mul(matrix_1, matrix_2):
    """Perform multiplication of two matrices.

    Args:
        matrix_1 (list of lists of ints/floats): The first matrix.
        matrix_2 (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either matrix_1 or matrix_2 is not a list of lists of
                     integers or floats.
        TypeError: If either matrix_1 or matrix_2 is empty.
        TypeError: If either matrix_1 or matrix_2 has different-sized rows.
        ValueError: If matrix_1 and matrix_2 cannot be multiplied.
    Returns:
        A new matrix resulting from the multiplication of matrix_1 by matrix_2.
    """

    if matrix_1 == [] or matrix_1 == [[]]:
        raise ValueError("m_a can't be empty")
    if matrix_2 == [] or matrix_2 == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(matrix_1, list):
        raise TypeError("m_a must be a list")
    if not isinstance(matrix_2, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in matrix_1):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in matrix_2):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in matrix_1 for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in matrix_2 for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(matrix_1[0]) for row in matrix_1):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(matrix_2[0]) for row in matrix_2):
        raise TypeError("each row of m_b must should be of the same size")

    if len(matrix_1[0]) != len(matrix_2):
        raise ValueError("m_a and m_b can't be multiplied")

    flipped_matrix_2 = []
    for row_idx in range(len(matrix_2[0])):
        new_row = []
        for col_idx in range(len(matrix_2)):
            new_row.append(matrix_2[col_idx][row_idx])
        flipped_matrix_2.append(new_row)

    product_matrix = []
    for row in matrix_1:
        new_row = []
        for col in flipped_matrix_2:
            element_product = 0
            for idx in range(len(flipped_matrix_2[0])):
                element_product += row[idx] * col[idx]
            new_row.append(element_product)
        product_matrix.append(new_row)

    return product_matrix
