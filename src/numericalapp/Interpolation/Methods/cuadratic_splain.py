import numpy as np
import sympy as sp


def splain(x, y):
    dimension = 3*len(x) - 3

    matrix = np.zeros((dimension, dimension))

    m = (dimension-len(y))
    b = np.append(y, np.zeros(m))

    interpolation(x, matrix)
    continuity(x, matrix)
    smoothness(x, matrix)
    borderline(matrix)

    np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})

    print('\033[96m')
    print('Cuadratic tracers coefficients')
    print('\033[0m')
    xact = np.linalg.solve(matrix, b)
    for i in range(0,len(matrix), 3):
        expr = f'{float("{:.5f}".format(xact[i]))} <-> {float("{:.5f}".format(xact[i+1]))} <-> {float("{:.5f}".format(xact[i+2]))}'
        print(expr)

    print('\033[96m')
    print('Cuadratic tracers')
    print('\033[0m')
    x = sp.symbols('x')
    for i in range(0,len(matrix), 3):
        expr = xact[i]*x*x + xact[i+1]*x + xact[i+2]
        print(expr)


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