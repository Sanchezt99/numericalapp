import numpy

class Jacobi:


    def evaluate(tol, niter, relajacion,matrix,m,indp,x0):
        matrix = matrix.copy()
        m = m
        etapas = []
        values = []
        x = numpy.empty(m)
        indp = indp.copy()
        x0 = x0.copy()
        x1 = numpy.empty(m)
        res = numpy.empty(m)
        aux = []
        dispersion = 0
        cont  = 0
        dispersion = float(tol + 1)

        values.append(["Step: " + str(cont), x0, dispersion])

        while (dispersion > tol) and (cont < niter):
            print("entro while")

            for i in range(m):
                x1[i] = x0.item(i)
            for i in range(m):
                suma = 0
                for j in range(m):
                    if j != i:
                        suma += (matrix.item(i, j)*x0.item(j))
                
                if matrix.item(i, i) != 0:
                    x1[i] = (indp.item(i) - suma)/matrix.item(i, i)
                else:
                    print("El sistema posiblemente no tiene solución")

                
            aux = x1 - x0
            dispersion = numpy.linalg.norm(aux)/numpy.linalg.norm(x1)
     
            if relajacion != 0:
                for i in range(len(x0)):
                    x1[i] = (relajacion*x1.item(i))+((1-relajacion)*x0.item(i))
                
            x0 = x1
            cont += 1

            print([cont, str(x0), dispersion])
            values.append(["Step: "+ str(cont), x0, dispersion])
        
        if dispersion < tol:
            print(f"{x1} es aproximación con una tolerancia = {tol}")
        else:
            print(f"Fracasó en {niter} iteraciones")
        return values