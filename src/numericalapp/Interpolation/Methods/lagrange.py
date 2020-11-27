import sympy as sp
from sympy.parsing.sympy_parser import parse_expr as pe


def lagrange(x,y):        
    n=len(x)
    print(n)
    print("Lagrange interpolating polynomials:")
    lk = []
    for i in range(len(x)):    
        print(i)
        l=''    
        denominator = 1
        for j in range(len(y)):
            if i!=j :
                denominator *= pe(f'1/({x[i]}-{-x[j]})')
                sign = '+' if -x[i] > 0 else '-'
                number = abs(x[j])
                l=f'{l}*(x{sign}{number})' if number != 0 else f'{l}*(x)'
        print(denominator,l)
    print("Lagrange polynom")
    for i in range(len(x)): 
        print(i)
        print(str(y[i])+"*L"+str(i),end='')
        if i<len(x)-1:
            print("+",end='')

x=[-1,0,3,4]
y=[15.5,3,8,1]
lagrange(x,y)