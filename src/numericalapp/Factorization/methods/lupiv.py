
import numpy as np
from sustprog import prog_sust, reg_sust,sustitucion_regresiva
import sys
import math

def LU(A):
    n = A.shape[0]
    L = np.identity(n).astype(np.float64)
    U = np.zeros((n,n)).astype(np.float64)
    M = A
    A = A.astype(np.float64)
    P = np.identity(n).astype(np.float64)
    print(f"Partial Pivot\n Stage 0 \n")
    np.savetxt(sys.stdout, A, fmt="%8.3f")
    print()


    for etapa in range(0,n-1):
        print(f"Stage {etapa+1} \n")
        a = np.absolute(A)
        maxindex = np.argmax(a[etapa::, etapa])
        b = a[etapa::, etapa]
        # print(b)
        # if maxindex != etapa:
        A[[etapa,maxindex+etapa]] = A[[maxindex+etapa,etapa]]
        P[[etapa,maxindex+etapa]] = P[[maxindex+etapa,etapa]]
        if etapa > 0:
            aux4 = np.copy(L[etapa, 0:etapa])
            # print(f"1 {aux4}")
            L[etapa, 0:etapa] = L[etapa+maxindex, 0:etapa]
            # print(f"2 {aux4}")
            L[etapa+maxindex, 0:etapa] = aux4
            # L[etapa, 0:etapa],L[etapa+maxindex, 0:etapa] = L[etapa+maxindex, 0:etapa],L[etapa, 0:etapa]
            # print(f" second aux4 {aux4}")
        
        for fila in range(etapa+1,n):
            if A[fila, etapa] != 0:
                L[fila,etapa] = A[fila,etapa]/ A[etapa,etapa]
                multiplicador = A[fila, etapa]/A[etapa,etapa]
                A[fila,etapa::] = (A[fila,etapa::] -((A[fila, etapa]/A[etapa,etapa]) * A[etapa,etapa::]))

        print("\n L: \n")
        np.savetxt(sys.stdout, L, fmt="%8.3f")


        U[etapa, etapa:n+1] = A[etapa,etapa:n+1]
        U[etapa+1,etapa+1:n+1] = A[etapa+1, etapa+1:n+1]
        U[-1,-1] = A[-1,-1]

        print("\n A: \n")
        np.savetxt(sys.stdout, A, fmt="%8.3f")
        print("\n P: \n")
        np.savetxt(sys.stdout, P, fmt="%8.3f")
        print("\n L: \n")
        np.savetxt(sys.stdout, L, fmt="%8.3f")
        print("\n U: \n")
        np.savetxt(sys.stdout, U, fmt="%8.3f")

    return L, U


def LU_pivpar(A,b):
    L, U = LU(A)
    lb = np.concatenate((L,b),axis=1)
    z = prog_sust(lb)
    z = z.reshape((z.shape[0],1))

    
    uz = np.concatenate((U,z), axis=1)

    x = sustitucion_regresiva(uz)
    print("After applying progresive and regresive sustitution\n X: ")
    np.savetxt(sys.stdout, x.transpose(), fmt="%8.3f")


def swap(ab,etapa):
    maxi = -math.inf
    maxindex = etapa
    n, p = ab.shape
    
    for i in range(etapa,n):
        if ab[i,etapa] > maxi:
    
            maxi = ab[i,etapa]
            maxindex= i

    ab[[etapa,maxindex]] = ab[[maxindex,etapa]]
    return ab

A = np.array([
    [4,3, -2, 7],
    [3,12,8,-3],
    [2,3,-9,3],
    [1,-2,-5,6]])

A = np.array([
    [4,-1, -10, 3],
    [1,15.5,3,8],
    [0,-1.3,-4,1.1],
    [14,5,-2, 30]])

A = np.array([
    [-7,2, -3, 4],
    [5,-1, 14,-1],
    [1,9,-7,5],
    [-12,13,-8, -4]])

A = np.array([
    [4,-1, 0, 3],
    [1,15.5,3,8],
    [0,-1.3,-4,1.1],
    [14,5,-2, 30]])

b = np.array([1 ,1 , 1, 1]).transpose().reshape(4,1)

def swap2(A,etapa):
    
    a = np.absolute(A)
    maxindex = np.argmax(a[etapa::, etapa])

    A[[etapa,maxindex+etapa]] = A[[maxindex+etapa,etapa]]
    return A

A = np.array([
    [4,-1, 0, 3],
    [1,15.5,3,8],
    [0,-1.3,-4,1.1],
    [14,5,-2, 30]])

b = np.array([1 ,1 , 1, 1]).transpose().reshape(4,1)

LU_pivpar(A,b)
# LU(A)


