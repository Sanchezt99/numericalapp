from numpy import array, diag, diagflat, dot
import  numpy as np
from numpy.linalg import inv



class Jacobii:

    def __init__(self,mat, b, n, error, itera):
        self.mat=mat
        self.b = b
        self.n = n
        self.error = error
        self.itera = itera



    def Jac(self):
        p = ""
        mat=self.mat.replace("[","")
        mat=mat.replace("]","")
        mat=mat.split(",")
        mat = np.array(mat)        
        mat = mat.astype(np.float)
        err = float(self.error)
        iterat = int(self.itera)
        n = int(self.n)
        mat = mat.reshape(n, n)

        b = self.b.split(",")

        for i in range(len(b)):
            b[i] = float(b[i])

        #A=array([[45.,-3.,-7.,8.],[-12.,36.,9.,-5.],[-6.,4.,57.,-8],[-3.,-5.,-10.,78.]])
        #b=array([1000.,-50.,300.,53.])
        guess=array([0.,0.,0.,0.])

        U=np.triu(mat,1)
        L=np.tril(mat,-1)
        D=diagflat(diag(mat))
        invD=inv(D)
        minLminU=-L-U
        
        for i in range(iterat):
            minLminUdotXplusB=dot(minLminU, guess) + b
            guess = dot(invD, minLminUdotXplusB)
            p+= str(i+1)+ " " +str(np.round(guess, 5))+"\n"
            e=np.linalg.norm(mat@guess-b)
            if e<err:
                break

        return p
