import numpy as np
import sympy as sp

def splain(x, y):

    x = np.array(x).astype(np.float)
    y = np.array(y).astype(np.float)

    dimension = 2*len(x) - 2

    matrix = np.zeros((dimension, dimension))
    m = (dimension-len(y))
    b = np.append(y, np.zeros(m))

    interpolation(x, matrix)
    continuity(x, matrix)

    np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

    print('\033[96m')
    print('Lineal tracers coefficients')
    print('\033[0m')
    xact = np.linalg.solve(matrix, b)

    coefficients = []
    for i in range(0,len(matrix), 2):
        coefficients.append[f'{float("{:.5f}".format(xact[i]))} <-> {float("{:.5f}".format(xact[i+1]))}']

    print('\033[96m')
    print('Lineal tracers')
    print('\033[0m')
    x = sp.symbols('x')
    tracers = []
    for i in range(0,len(matrix), 2):
        expr = xact[i]*x + xact[i+1]
        tracers.append(sp.pretty(expr))

    return tracers, coefficients



def interpolation(x, matrix):

    matrix[0][0] = x[0] 
    matrix[0][1] = 1

    xn = 1
    i = 0
    for j in range(1, len(x)):
        matrix[j][i]   = x[xn]
        matrix[j][i+1] = 1
        i += 2
        xn += 1

def continuity(x, matrix):
    start = len(x)
    dimension = len(matrix)


    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i]   = x[xn]
        matrix[j][i+1] = 1
        matrix[j][i+2] = -x[xn]
        matrix[j][i+3] = -1
        xn += 1
        i += 2