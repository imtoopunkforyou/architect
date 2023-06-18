from typing import List


def matrix_multiplication(matrix1: List[list],
                          matrix2: List[list]) -> List:
    try:
        result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result
    except IndexError as exc:
        raise IndexError('Incompatible matrix sizes') from exc


if __name__ == '__main__':
    a = [
        [6, -8, 3],
    ]
    b = [
        [1],
        [1],
        [4],
    ]
    c = [
        [-3, -7],
        [-10, 6],
        [0, -6],
        [-1, -3],
    ]
    d = [
        [-8, 9],
        [4, -2],
    ]

    print(f'First task result:\n{matrix_multiplication(a, b)}\n')
    print(f'Second task result:\n{matrix_multiplication(c, d)}\n')
