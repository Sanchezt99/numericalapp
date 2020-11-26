import numpy as np

class Jacobi:


    def evaluate(A, b, x0,tol,interaciones):
        ans = []
        errorma = []
        D= np.diag(np.diag(A))
        D1 = np.diag(1/np.diag(A))
        U=np.triu(A,1)
        L=np.tril(A,-1)
        B= L + U
        LU = A-D
        T=(np.dot(-D1,B))
        C=(np.dot(D1,b))

        x = x0

        # print(x0)
        error = tol + 1
        for i in range(interaciones):
            D_inv = np.linalg.inv(D)
            xtemp = x
            x = np.dot(D_inv, np.dot(-(LU),x) + b)
            ans.append(x)
            error = np.linalg.norm(x-xtemp)
            errorma.append(error)
            
            if np.linalg.norm(x-xtemp)<tol:
                
                return ans,errorma,T,C
        
        return ans,errorma,T,C
