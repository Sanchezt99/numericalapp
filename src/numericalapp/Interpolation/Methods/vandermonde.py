import numpy as np
from utils import MatrixUtils as mu

def Vandermonde(x,y):

    x = np.array(x).astype(np.float)
    y = np.array(y).astype(np.float)

    if not mu.checkUnique(x):
        return None, None, 'X vector can\'t contain repeated values'

    n=len(x)
    A=np.ones((n,n))
    vPolynomial = []
    message = 'Successful'

    for i in range(n):
        A[:,i]=x**(n-(i+1))
    print('Vandermonde Matrix:')
    coefficients = np.dot(np.linalg.inv(A),y)
    for i in range(len(coefficients)):
        if i == len(coefficients)-1:
            vPolynomial.append(f'{str(coefficients[i])}*x^{len(coefficients)-(i+1)}')
        else:
            vPolynomial.append(f'{str(coefficients[i])}*x^{len(coefficients)-(i+1)}+')
    return A, vPolynomial, message


x = [-1,0,3,4]
y = [15.5,3,8,1]
Vandermonde(x,y)
