#!/user/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in ramge(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
        return (new_matrix)
