import numpy as np


# rotate matrix by 90 degrees
def rotate_matrix(matrix):
    print(np.matrix(matrix))
    print()

    new_matrix = [[0 for i in range(3)] for i in range(3)]
    row = len(matrix[0]) - 1
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):
            new_matrix[j][row] = matrix[i][j]

        row = row-1
    print(np.matrix(new_matrix))


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

rotate_matrix(matrix)
