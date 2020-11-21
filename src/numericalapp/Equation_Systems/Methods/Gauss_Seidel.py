import  numpy as np

class GaussSeidel:

    def __init__(self,mat, b, n, error, itera):
        self.mat=mat
        self.b = b
        self.n = n
        self.error = error
        self.itera = itera

#A=np.array([[15,-7,2],
#            [-4,20,-16],
#            [13,-4,45],])
#b=np.array([5.,34.,-23.])

    def GaussS(self):
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

        x=np.zeros_like(b)

        for k in range(iterat):
            for i in range(len(b)):
                x[i]=(b[i]-np.sum(mat[i][:i]*x[:i])-np.sum(mat[i][i+1:]*x[i+1:]))/mat[i][i]

            e=np.linalg.norm(mat@x-b)
            print(k,x,e)
            if e<err:
                break

        return x	 
