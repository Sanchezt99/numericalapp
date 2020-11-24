import numpy as np

def gauss_enter(a,size):
    print(f"a {a} \n size {size}")
    A = a[0:-size]
    b = a[-size::]
    print(f"A {A} \n b {b}")
    A = np.array(A).reshape(size,size).astype(np.float64)
    b = np.array(b).reshape(size,1).astype(np.float64)
    return A,b




def gauss_elimination(a,b):
    print("enter gauss")
    message = ""
    etapas = []
    matrixs = []
    if a.shape[0] != a.shape[1]:
        message += "Matrix A has to be square"
        # file1.write("La matriz A debe ser cuadrada")
        # file1.close()
        # return message
    
    if a.shape[1] != b.shape[0]:
        message += "The number of columns of A must be the same as the number of rows of b"
        # file1.write("El número de columnas de A debe ser el mismo al número de filas de b")
        # file1.close()
        # return message
    
    if np.linalg.det(a) == 0:
        message = "Determinant of A must be different from zero"
        # file1.write("El determinante de A debe ser diferente de 0")
        # file1.close()
        # return message

    if not message:
        ns = "\n"*2
        ab = np.concatenate((a,b), axis=1)
        n,p = ab.shape
        # file1.write("Eliminación Gaussiana Simple \n Etapa 0 \n") 
        ab = np.around(ab,6)
        # file1.write(str(ab))
        # file1.write(ns)    

        #ab.astype(float64)
        if ab[0,0] == 0:
            swap(ab,0,0)
        
        for etapa in range(0,n-1):
            etapas.append(etapa)
            # file1.write(eta )
            if ab[etapa,etapa] == 0:
                ab = swap(ab,etapa)
            for fila in range(etapa+1,n):
                ab[fila,etapa::] = (ab[fila,etapa::] -(ab[fila, etapa]/ab[etapa,etapa] * ab[etapa,etapa::]))
            
            ab = np.around(ab,6)
            matrixs.append(ab)
            # file1.write(str(ab))
            
            # file1.write(ns)
            # #break
        
        x = sust_reg(ab)
    # file1.write("Después de sustitución regresiva:\n x:\n")
    # file1.write(str(x.T))
    return message, etapas, matrixs
    
def swap(ab,etapa):
    n, p = ab.shape
    for i in range(etapa+1,n):
        if ab[i,etapa] != 0:
            ab[[etapa,i]] = ab[[i,etapa]]
            return ab


def sust_reg(ab):
    n = ab.shape[0]
    
    x = np.zeros((1,n))
    x[0,n-1] = ab[n-1,n]/ab[n-1,n-1]
    

    for i in range(n-2,-1,-1):
        print("\n i",i)
        aux = np.array([np.append( 1, x[0,i+1:n+1])])
        aux1 = np.array([np.append(ab[i,n],-1 * ab[i,i+1:n])]).T
        x[0,i] = np.dot(aux,aux1)/ab[i,i]

    return x