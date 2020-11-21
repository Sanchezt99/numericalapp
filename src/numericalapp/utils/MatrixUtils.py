import numpy as np
import pprint
import scipy
import scipy.linalg

def dispersion(x,deltaX):
    resultado=list(range(len(x)))

    for a in range(len(x)):
        resultado[a]=abs(deltaX-x)

    return resultado


def mayorError(x):
    mayor=x[0]
    for a in x:
        if a > mayor:
            mayor=a
    return a

def encontrarx(mat,x):
    print(mat)
    print(x)
    resultado=list(range(len(mat)))
    for a in range(len(mat)):
        cont = 0
        for b in range(len(mat)):
            if b!=a:
                cont-=(mat[a][b]*x[b])
        cont+=mat[a][len(mat)-1]
        print(str(cont))
        print(str(mat[a][a]))
        cont=cont/x[a]
        resultado[a]=cont
    print(resultado)
    return resultado

def plu(mat):
    P, L, U = scipy.linalg.lu(mat)
    return P,L,U

def susre(Ab):
    n = len(Ab)
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        sumatoria = 0
        for p in range(i+1,n):
            sumatoria += Ab[i][p]*x[p]
        
        x[i] = (Ab[i][n]-sumatoria)/float(Ab[i][i])
    return x

def suslu(Ab):
    n = len(Ab)
    x = np.zeros(n)
    for i in range(n):
        sumatoria = 0
        for p in range(n):
            sumatoria += Ab[i][p]*x[p]
        print(sumatoria)
        x[i] = (Ab[i][n]-sumatoria)/float(Ab[i][i])
    return x


def printmat(x):

    for i in range(len(x)):
        for j in range(len(x)):
            print(str(x[i][j])+", ",end = "")
        print("= "+str(x[i][len(x)])+"\n")
    print("\n\n\n\n_________________")