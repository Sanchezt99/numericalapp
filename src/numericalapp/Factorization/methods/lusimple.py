
import numpy as np
from .sustprog import prog_sust, reg_sust,sustitucion_regresiva
import sys

def LU_enter(a,size):
    A = a[0:-size]
    b = a[-size::]
    print(f"A {A} \n b {b}")
    A = np.array(A).reshape(size,size).astype(np.float64)
    b = np.array(b).reshape(size,1).astype(np.float64)
    return A,b


def LU(A):
    n = A.shape[0]
    L = np.identity(n)
    U = np.zeros((n,n))
    M = A
    A = A.astype(np.float64)
    L = L.astype(np.float64)
    U = U.astype(np.float64)

    A_list = []
    L_list = []
    U_list = []
    # print(f"Etapa 0 \n")
    A_list.append(np.round(A,3))
    # np.savetxt(sys.stdout, A, fmt="%8.3f")
    # print()

    message = ""
    for etapa in range(0,n-1):
        print(f"Etapa {etapa+1} \n")
        if A[etapa,etapa] == 0:

            message = "A connot have 0 in its diagonal"

            return message, [], [], []

        for fila in range(etapa+1,n):
            if A[fila, etapa] != 0:
                L[fila,etapa] = A[fila,etapa]/ A[etapa,etapa]
                multiplicador = A[fila, etapa]/A[etapa,etapa]
                A[fila,etapa::] = (A[fila,etapa::] -((A[fila, etapa]/A[etapa,etapa]) * A[etapa,etapa::]))

        U[etapa, etapa:n+1] = A[etapa,etapa:n+1]
        U[etapa+1,etapa+1:n+1] = A[etapa+1, etapa+1:n+1]

        np.savetxt(sys.stdout, A, fmt="%8.3f")
        A_list.append(np.round(A,3))
        L_list.append(np.round(L,3))
        U_list.append(np.round(U,3))
        # print("L:")
        # np.savetxt(sys.stdout, L, fmt="%8.3f")
        # print("U:")
        # np.savetxt(sys.stdout, U, fmt="%8.3f")
        # print()

        # print(A)
        # print(U)

    U[-1,-1] = A[-1,-1]
    print(A)
    print("U matrix")
    print(U)


    U_list.append(np.round(U,3))
    
    return message, A_list, L_list, U_list, L, U

def LU_simple(A,size):
    A, b = LU_enter(A,size)
    message, A_lista, L_lista, U_lista, L, U = LU(A)

    if message:
        return message, [], [], [], [], []

    lb = np.concatenate((L,b),axis=1)
    z = prog_sust(lb)
    z = z.reshape((z.shape[0],1))
  
    uz = np.concatenate((U,z), axis=1)
    print("Uz \n")
    print(uz)
    print("x")
    x = sustitucion_regresiva(uz).tolist()

    final = []
    if A_lista:
        for i in range(len(A_lista)-1):
            m = []
            m.append(A_lista[i])
            m.append(L_lista[i])
            m.append(U_lista[i])
            final.append(m)

    return message, A_lista, L_lista , U_lista, x, final
   



