import numpy as np
import sympy as sp
from utils import MatrixUtils as mu


def splain(x, y):


    x = np.array(x).astype(np.float)
    y = np.array(y).astype(np.float)

    if not mu.checkUnique(x):
        return None, None, 'X vector can\'t contain repeated values'


    dimension = 4*len(x) - 4

    matrix = np.zeros((dimension, dimension))

    m = (dimension-len(y))
    b = np.append(y, np.zeros(m))


    interpolation(x, matrix)
    continuity(x, matrix)
    smoothness(x, matrix)
    convexSet(x, matrix)
    borderlineOne(x, matrix)
    borderlineTwo(x, matrix)

    np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

    xact = np.linalg.solve(matrix, b)
    coefficients = []
    count = 1
    for i in range(0,len(matrix), 4):
        expr = f'a{count} = {float("{:.5f}".format(xact[i]))}, b{count} = {float("{:.5f}".format(xact[i+1]))}, c{count} = {float("{:.5f}".format(xact[i+2]))}, d{count} = {float("{:.5f}".format(xact[i+3]))}'
        coefficients.append(expr)

    xv = sp.symbols('x')
    tracers = []
    for i in range(0,len(matrix), 4):
        expr = float("{:.5f}".format(xact[i]))*xv*xv*xv + float("{:.5f}".format(xact[i+1]))*xv*xv + float("{:.5f}".format(xact[i+2]))*xv + float("{:.5f}".format(xact[i+3]))
        tracer = [sp.latex(expr)]
        tracers.append(tracer)

    for i in range(len(x)-1):
        tracers[i].append(f'{x[i]} <= x <= {x[i+1]}')

    return tracers, coefficients, 'Successful'
    


def interpolation(x, matrix):

    matrix[0][0] = pow(x[0], 3)
    matrix[0][1] = pow(x[0], 2)
    matrix[0][2] = x[0]
    matrix[0][3] = 1

    xn = 1
    i = 0
    for j in range(1, len(x)):
        matrix[j][i]   = pow(x[xn], 3)
        matrix[j][i+1] = pow(x[xn], 2)
        matrix[j][i+2] = x[xn]
        matrix[j][i+3] = 1
        i += 4
        xn += 1


def continuity(x, matrix):
    start = len(x)
    dimension = 2*len(x) - 2

    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i]   = pow(x[xn],3)
        matrix[j][i+1] = pow(x[xn],2)
        matrix[j][i+2] = x[xn]
        matrix[j][i+3] = 1
        matrix[j][i+4] = -pow(x[xn],3)
        matrix[j][i+5] = -pow(x[xn],2)
        matrix[j][i+6] = -x[xn]
        matrix[j][i+7] = -1
        xn += 1
        i += 4


def smoothness(x, matrix):
    start = 2*len(x) - 2
    dimension = 3*len(x) - 4

    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i]   = 3*pow(x[xn],2)
        matrix[j][i+1] = 2*x[xn]
        matrix[j][i+2] = 1
        matrix[j][i+4] = -3*pow(x[xn],2)
        matrix[j][i+5] = -2*x[xn]
        matrix[j][i+6] = -1

        xn += 1
        i  += 4

def convexSet(x, matrix):
    start = 3*len(x) - 4
    dimension = len(matrix) - 2

    xn = 1
    i = 0
    for j in range(start, dimension):
        matrix[j][i]   = 6*x[xn]
        matrix[j][i+1] = 2
        matrix[j][i+4] = -6*x[xn]
        matrix[j][i+5] = -2

        xn += 1
        i  += 4


def borderlineOne(x, matrix):
    border = [6*x[0],2]
    m = len(matrix) - 2
    b = np.append(border, np.zeros(m))
    matrix[m] = b

def borderlineTwo(x, matrix):
    last = len(x) - 1
    border = [6*x[last], 2, 0 , 0]
    m = len(matrix) - 4
    b = np.append(np.zeros(m), border)
    matrix[len(matrix)-1] = b


x = np.array([-1,0,1,2])
y = np.array([1,1,2,10])

splain(x,y)