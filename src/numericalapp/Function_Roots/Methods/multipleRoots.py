import math
from scitools.StringFunction import StringFunction


def multiple_roots(f,fprima, f2prima,tol,N,x0):
    # print("Raices multiples \n")
    # print(" iter|      xi         |      f(xi)      |       E       ")
    
    #se inicializa los valores iniciales
    
    ansTable = []
    x = x0
    fun = StringFunction(f)
    func = fun(x)
    fun_prima = StringFunction(fprima)
    func_prima = fun_prima(x)
    fun_2prima = StringFunction(f2prima)
    func_2prima = fun_2prima(x)
    error = math.inf

    ansTable.append(["i", "xi",  "f(xi)", "E"])

    if func == 0:
        # print(f"{x0} is the root")
        return f"{x0} is the root"
    if N < 1:
        # print("The iterator value is wrong")
        return "The iterator value is wrong"
    if tol < 0:
        # print("Tolerance error, must be greater than or equal to 0")
        return "Tolerance error, must be greater than or equal to 0"



    print("{:4} | {:15e} | {:15e} | ".format(0, x, func))

    ansTable.append([str(0), str(x), str(func), ' '])
    #print(str(0).ljust(5) + "|" + str(x).ljust(22) + '|'+ str(func).ljust(22) + "|" )

    #se calcula x hasta la iteracion N o hasta que el error sea <= a tol
    for i in range(N):
        if error <= tol:
           break
        error = abs(x)
        x = x - (func * func_prima) / ( (func_prima**2) - (func * func_2prima))
        
        fun = StringFunction(f)
        func = fun(x)
        fun_prima = StringFunction(fprima)
        func_prima = fun_prima(x)
        fun_2prima = StringFunction(f2prima)
        func_2prima = fun_2prima(x)
        error = abs(error-x)

        ansTable.append([str(i+1), str(x), str(func), str(error)])
        # print("{:4} | {:15e} | {:15e} | {:15e}".format(i+1,x,func,error))

        #print(str(i+1).ljust(5) + "|" + str(round(x,5)).ljust(22) + '|'+ str(round(func,5)).ljust(22) + "|" + str(round(error,5)).ljust(22) )

    
    print("\nA root approximation was found at", x)

    return ansTable, x
