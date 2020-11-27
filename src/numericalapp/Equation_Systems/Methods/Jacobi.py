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
        T= Jacobi.duoTC(np.dot(-D1,B))
        C= Jacobi.duoTC(np.dot(D1,b))
        message = ''
        x = x0

        # print(x0)
        error = tol + 1
        for i in range(0,len(A.diagonal())):
            if A.diagonal()[i] == 0:
                message = "ERROR: Diagonal can't have a 0"
                return None, None,None,None,message
        if(np.linalg.det(A) == 0):
            message="ERROR: Determinant of matrix A is 0"
            return None,None,None,None,message

        for i in range(interaciones):
            D_inv = np.linalg.inv(D)
            xtemp = x
            x = np.dot(D_inv, np.dot(-(LU),x) + b)
            ans.append(Jacobi.duoarr(x))
            error = np.linalg.norm(x-xtemp)
            errorma.append(format(error,",.2e"))
            
            if np.linalg.norm(x-xtemp)<tol:
                
                return ans,errorma,T,C,"Successful"
        
        return ans,errorma,T,C,"Successful"




    def duoarr(x):
        n=[]
        for i in x:
            for j in i:
                n.append(round(j,7))
        return n

    def duoTC(x):
        n=[]
        for i in x:
            m=[]
            for j in i:
                m.append(round(j,5))
            n.append(m)
        n=np.array(n)
        return n