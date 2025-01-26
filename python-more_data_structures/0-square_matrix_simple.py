#  Creates a new matrix where each value is the square of the original matrix
def square_matrix_simple(matrix=[]):  # This defines the prototype
    return [[value ** 2 for value in row] for row in matrix]
