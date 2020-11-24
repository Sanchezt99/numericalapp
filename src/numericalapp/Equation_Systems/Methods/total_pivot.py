import utils.MatrixUtils as mu
import numpy as np

def gauss(matrix, b):
    positionStamp = [0] * len(matrix)

    for i in range(len(positionStamp)):
        positionStamp[i] = i

    for i in range(len(matrix)):
        pivot(matrix, i, b, positionStamp)

        for j in range(i+1,len(matrix)):
            multiplicand = matrix[j][i] / matrix[i][i]
            elimination(i, j, multiplicand, matrix, b)
    return sort(backwardSubstitution(matrix, b), positionStamp)


def pivot(matrix, index, b, positionStamp):
    row = index
    col = index

    for i in range(row, len(matrix)):
        for j in range(col, len(matrix)):
            if abs(matrix[j][i]) > abs(matrix[row][col]):
                row = j
                col = i
    if col != index:
        mu.swapCols(matrix, col, index)
        mu.swapValues(positionStamp, col, index)
    if row != index:
        mu.swapRows(matrix, row, index)
        mu.swapValues(b, row, index)

def sort(values, positions):
    sortedValues = [0] * len(values)
    for i in range(len(positions)):
        sortedValues[positions[i]] = values[i]
    return sortedValues


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
