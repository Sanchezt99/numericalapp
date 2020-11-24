import numpy

class Doolittle:



    def evaluate(matrix,m,indp):
        U =  numpy.identity(m)
        L =  numpy.identity(m)
        x = numpy.empty(m)
        z = numpy.empty(m)
        matrixs = []
        
        # print(U)
        # print(L)
        # print(matrix)

        for fila in range(m):
            suma1 = 0
            for columna in range(fila):
                suma1 += L.item(fila, columna)*U.item(columna, fila)
            
            #L.[fila,fila] = 1

            U[fila, fila] = matrix.item(fila, fila) - suma1

            #etapas.append(matrix.copy())

            #for s in range(m -1):
            #    print(etapas[s])


            for i in range(fila+1, m):
                suma2 = 0
                
                for columna in range(fila):
                    suma2 += L.item(i, columna)*U.item(columna, fila)
                if L.item(fila, fila)!=0:
                    L[i, fila] = float(matrix.item(i, fila) - suma2)/U.item(fila,fila)
                    matrixs.append(L.copy()) 
                    print(len(matrixs))
                else:
                    return("Possibly there is no solution for this problem")
                
            for j in range(fila+1,m):
                suma3 = 0
                for columna in range(fila):
                    suma3 += L.item(fila, columna)*U.item(columna, j)

                if L.item(fila, fila)!=0:  
                    
                    U[fila, j] = float(matrix.item(fila, j) - suma3)
                    matrixs.append(U.copy())
                else:
                    return("Possibly there is no solution for this problem")
                    
                
        
       

        detU = 1
        detL=1
        for each in U.diagonal(0,0):
            detU*= each
        
        prod = detU * detL
        if prod != 0:
            for i in range(m):
                suma = 0
                for p in range(i):
                    suma+= (L.item(i,p)*z.item(p))
                z[i] = (indp.item(i)-suma)/L.item(i,i)

            for i in range(m-1,-1,-1):
	            suma=0
	            for p in range(i+1,m):
		            suma=suma+(U.item(i,p)*x.item(p))
	            x[i]=float((z.item(i)-suma)/U.item(i,i))
            
        else:
            print("The Det is equal to 0, so there can be none solutions or infinite ones.")
            return
        print(matrixs)
        # print(f"L:\n {L}\n\nU:\n{U}\n")
        matrixs.append((L))
        matrixs.append(U)
        matrixs.append(x)
        # for each in range(m):
        #     print(f"x{each} = {x[each]}")
    
        return matrixs