matrix = [[2, 0, 1],
          [-3, 1, 2],
          [0, 1, 5]]


def is_square(matrix):
    for i in matrix:
        if len(i) != len(matrix):
            return False
    return True


def submatrix(matrix, col):
    return [row[:col] + row[col + 1:] for row in matrix[1:]]


def calculate(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        det: int = 0
        for col in range(len(matrix)):
            det += (matrix[0][col] * (-1) ** col) * calculate(submatrix(matrix, col))
    return det


if __name__ == "__main__":
    if is_square(matrix):
        print("The determinant of the matrix is: ", calculate(matrix))
    else:
        print("The matrix is not square")
