import numpy as np
import sympy as sym


xi = []
fi = []

n=int(input("Enter the number of data to use: "))
for i in range(n):
    x=float(input("Enter the value of Xi "))
    xi.append(x)
    f=float(input("Enter the value of Yi "))
    fi.append(f)

xi=np.array(xi)
fi=np.array(fi)

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

px = sym.lambdify(x,polisimple)


np.set_printoptions(precision = 4)

print('Newton’s polynomial coefficients: ')
print(term)
print('Newton’s Divided Difference Table')
print(salida)

print(' Newton’s polynom: ')
print(polinomio)
print('Newton’s simple polynom:: ' )
print(polisimple)
