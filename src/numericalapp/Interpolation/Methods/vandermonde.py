import numpy as np

def Vandermonde(X,Y):
    n=len(X)
    A=np.ones((n,n))

    for i in range(n):
        A[:,i]=X**(n-(i+1))
    print('Vandermonde Matrix:')
    print(A)
    return  np.dot(np.linalg.inv(A),Y)

n=int(input('Enter the number of data to use: '))
X=np.zeros(n)
Y=np.zeros(n)
print('Values ​​must be introduced by couples(X,Y)')

for i in range(n):
    print('Enter the value of X[',i,']')
    X[i]=float(input())
    print('Enter the value of Y[',i,']')
    Y[i]=float(input())

coef=Vandermonde(X,Y)
print('Polynomial coefficients: ', coef)
print('Vandermonde polynom: ')
n = len(coef)
for i in range(n):
    print(coef[i],"*x^",n-(i+1),"+")
