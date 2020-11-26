import numpy as np
import sympy as sp
from utils import MatrixUtils as mu

def splain(x, y):

    x = np.array(x).astype(np.float)
    y = np.array(y).astype(np.float)

    if not mu.checkUnique(x):
        return None, None, 'X values must be unique between them' 

    dimension = 2*len(x) - 2

    matrix = np.zeros((dimension, dimension))
    m = (dimension-len(y))
    b = np.append(y, np.zeros(m))

    interpolation(x, matrix)
    continuity(x, matrix)

    np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})


    xact = np.linalg.solve(matrix, b)
    coefficients = []
    for i in range(0,len(matrix), 2):
        expr = f'a{i+1} = {float("{:.5f}".format(xact[i]))}, b{i+1} = {float("{:.5f}".format(xact[i+1]))}'
        coefficients.append(expr)

    xv = sp.symbols('x')
    tracers = []
    for i in range(0,len(matrix), 2):
        expr = float("{:.5f}".format(xact[i]))*xv + float("{:.5f}".format(xact[i+1]))
        tracer = [sp.latex(expr)]
        tracers.append(tracer)

    for i in range(len(x)-1):
        tracers[i].append(f'{x[i]} <= x <= {x[i+1]}')

    return tracers, coefficients, 'Successful'



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