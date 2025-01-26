def square_matrix_simple(matrix=[]):
    # Handle cases where matrix is empty or contains empty rows
    if not matrix:
        return []
    return [[value * value for value in row] for row in matrix]
