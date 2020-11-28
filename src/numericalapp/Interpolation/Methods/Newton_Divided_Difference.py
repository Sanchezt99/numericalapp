import numpy as np
import sympy as sym
from utils import MatrixUtils as mu

def evaluate (x , y):
    n=len(x)
    print(float(x[0]))
    if not mu.checkUnique(x):
        message = "The values in the vectors have to be unique "
        return None,None,None,None, message
    xi=np.zeros(n)
    fi=np.zeros(n)
    for i in range(0,len(x)):
        xi[i] =float(x[i])
    
    for i in range(0,len(y)):
        fi[i] =float(y[i])
    
    
    print(xi)
    n = len(xi)
    ki = np.arange(0,n,1)
    tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
    tabla = np.transpose(tabla)

    dfinita = np.zeros(shape=(n,n),dtype=float)
    tabla = np.concatenate((tabla,dfinita), axis=1)
    [n,m] = np.shape(tabla)
    diagonal = n-1
    j = 3
    while (j < m):
        i = 0
        paso = j-2 
        while (i < diagonal):
            denominador = (xi[i+paso]-xi[i])
            numerador = tabla[i+1,j-1]-tabla[i,j-1]
            tabla[i,j] = numerador/denominador
            i = i+1
        diagonal = diagonal - 1
        j = j+1

    dDividida = tabla[0,3:]
    term=tabla[0,2:6]
    n = len(dfinita)


    x = sym.Symbol('x')
    polinomio = fi[0]
    for j in range(1,n,1):
        factor = dDividida[j-1]
        termino = 1
        for k in range(0,j,1):
            termino = termino*(x-xi[k])
        polinomio = polinomio + termino*factor
        
    salida=np.zeros(shape=(n,n))

    for i in range(n):
        for j in range(n):
            salida[i,j]=tabla[i-j,j+2]

    polisimple = polinomio.expand()


    np.set_printoptions(precision = 4)

    return term,salida, str(polinomio),str(polisimple), None
