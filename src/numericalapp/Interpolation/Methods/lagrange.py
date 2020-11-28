from sympy.parsing.sympy_parser import parse_expr as pe
from utils import MatrixUtils as mu
import numpy as np


def lagrange(x,y):
    x = np.array(x).astype(np.float)
    y = np.array(y).astype(np.float)
    lps = []
    lp = []
    message = 'Successful'

    if not mu.checkUnique(x):
        return None, None, 'X vector can\'t contain repeated values'

    for i in range(len(x)):
        l=''    
        denominator = 1
        for j in range(len(y)):
            if i!=j :
                denominator *= pe(f'1/{x[i]-x[j]}')
                sign = '+' if -x[i] > 0 else '-'
                number = abs(x[j])
                l=f'{l}*(x{sign}{number})' if number != 0 else f'{l}*(x)'
        lps.append(str('{:.5f}'.format(denominator)) + l)
    
    for i in range(len(x)): 
        lp.append(f'{y[i]}*({lps[i]})')
    return lps, lp, message

x = [1,2,3,4]
y = [5,6,7,8]

lagrange(x,y)