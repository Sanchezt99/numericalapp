import numpy as np
import sympy as sp
from utils import MatrixUtils as mu


def splain(x, y):

    x = np.array(x).astype(np.float)
    y = np.array(y).astype(np.float)

    if not mu.checkUnique(x):
        return None, None, 'X vector can\'t contain repeated values'

    dimension = 3*len(x) - 3

    matrix = np.zeros((dimension, dimension))

    m = (dimension-len(y))
    b = np.append(y, np.zeros(m))

    interpolation(x, matrix)
    continuity(x, matrix)
    smoothness(x, matrix)
    borderline(matrix)

    np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

    xact = np.linalg.solve(matrix, b)
    coefficients = []
    count = 0
    for i in range(0,len(matrix), 3):
        expr = f'a{count} = {float("{:.5f}".format(xact[i]))}, b{count} = {float("{:.5f}".format(xact[i+1]))}, c{count} = {float("{:.5f}".format(xact[i+2]))}'
        coefficients.append(expr)

    xv = sp.symbols('x')
    tracers = []
    for i in range(0,len(matrix), 3):
        expr = float("{:.5f}".format(xact[i]))*xv*xv + float("{:.5f}".format(xact[i+1]))*xv + float("{:.5f}".format(xact[i+2]))
        tracer = [sp.latex(expr)]
        tracers.append(tracer)
    
    for i in range(len(x)-1):
        tracers[i].append(f'{x[i]} <= x <= {x[i+1]}')
        
    return tracers, coefficients, 'Successful'


def interpolation(x, matrix):

    matrix[0][0] = pow(x[0], 2)
    matrix[0][1] = x[0]
    matrix[0][2] = 1

    xn = 1
    i = 0
    for j in range(1, len(x)):
        matrix[j][i]   = pow(x[xn], 2)
        matrix[j][i+1] = x[xn]
        matrix[j][i+2] = 1
        i += 3
        xn += 1


def continuity(x, matrix):
    start = len(x)
    dimension = 2*len(x) - 2

    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i]   = pow(x[xn],2)
        matrix[j][i+1] = x[xn]
        matrix[j][i+2] = 1
        matrix[j][i+3] = -pow(x[xn],2)
        matrix[j][i+4] = -x[xn]
        matrix[j][i+5] = -1
        xn += 1
        i += 3


def smoothness(x, matrix):
    start = 2*len(x) - 2
    dimension = len(matrix) - 1

    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i]   = 2*x[xn]
        matrix[j][i+1] = 1
        matrix[j][i+3] = -2*x[xn]
        matrix[j][i+4] = -1
        xn += 1
        i  += 3

def borderline(matrix):
    border = [2]
    m = len(matrix)-1
    b = np.append(border, np.zeros(m))
    matrix[m] = b
    
    

x = np.array([-1,0,3,4])
y = np.array([15.5,3,8,1])

splain(x,y)