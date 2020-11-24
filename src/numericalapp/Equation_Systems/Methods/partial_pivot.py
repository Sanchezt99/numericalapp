import utils.MatrixUtils as mu
import numpy as np

def gauss(matrix, b):

    matrix = np.array(matrix).astype(np.float)
    b      = np.array(b).astype(np.float)



    for i in range(len(matrix)):
        pivot(matrix, i, b)

        for j in range(i+1,len(matrix)):
            multiplicand = matrix[j][i] / matrix[i][i]
            elimination(i, j, multiplicand, matrix, b)
    return backwardSubstitution(matrix, b)


def pivot(matrix, index, b):

    champion = index
    for i in range(len(matrix)):
        if abs(matrix[i][index]) > abs(matrix[champion][index]):
            champion = i
    if champion != index:    
        mu.swapRows(matrix, champion, index)
        mu.swapValues(b, champion, index)


a = [   [ 2,  -1, 0, 3],
        [ 1, 0.5, 3, 8],
        [0,   13, -2, 11],
        [14,   5, -2, 3]
    ]


def elimination(row1, row2, multiplicand, matrix, b):
    for i in range(len(matrix[row2])):
        matrix[row2][i] -= multiplicand*matrix[row1][i]

    b[row2] -= multiplicand*b[row1]


def backwardSubstitution(matrix, b):
    results = [0] * len(matrix)
    term = len(matrix) - 1

    for i in range(len(matrix)-1, -1, -1):
        left = [0] * (len(matrix) - i)
        for j in range(len(left)):
            left[j] = matrix[i][term-j]
        results[i] = backwardSolve(left=left, xValues=results, right=b[i])
    return results


def backwardSolve(left, xValues, right):
    if (len(left) == 1):
        return right/left[0]
    else:
        newRight = right - left[0]*xValues[len(xValues)-1]
        newLeft = np.copy(left)
        newLeft = np.delete(newLeft,0)
        newXValues = np.copy(xValues)
        newXValues = np.delete(newXValues,len(xValues)-1)
        return backwardSolve(left=newLeft, xValues=newXValues, right=newRight)
