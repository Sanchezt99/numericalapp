import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr as pe

class Secant:
    def __init__(self):
        self.values = []

    def evaluate(self, tol, x0, x1, fun, niter, type_error=0):

       # print("Iter", "xi", "f(xi)", "E")    

        ansTable = [] 
        ansTable.append(["i", "xi", "f(xi)", "E"])

        x = sp.symbols('x') #x0

        function = pe(fun)
        fx0 = function.subs(x,x0)

        

        if fx0 == 0:
            return f"{x0} is the root"
        else:
            fx1 = function.subs(x,x1)
            cont = 2
            
            error = tol + 1
            den = fx1 - fx0


            #print(0, x0, fx0)
            z = sp.symbols('z') #x2
            x2 = x1 - (fx1*(x1 - x0)/den)

            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = function.subs(x,x2)
            den = fx1 - fx0
            #print(1, x0, fx0)
            

            while error > tol and fx1 != 0 and den != 0 and cont < niter:

                
                x2 = x1 - (fx1*(x1 - x0)/den)
                
                if type_error == 0:
                    error = abs(x1-x0)
                else:
                    error = abs((x1-x0)/x1)

                x0 = x1
                fx0 = fx1
                x1 = x2
                fx1 = function.subs(x,x2)
                den = fx1 - fx0

                #print(cont, x0, fx0, error)
                cont += 1
                if x1 == 0 and fx1 != 0 and error != 0:
                    ansTable.append([cont, x1, "{0:0.9e}".format(fx1), "{0:0.2e}".format(error)])
                elif x1 != 0 and fx1 == 0 and error != 0:
                    ansTable.append([cont, "{0:0.9e}".format(x1), fx1, "{0:0.2e}".format(error)])
                elif x1 != 0 and fx1 != 0 and error == 0:
                    ansTable.append([cont, "{0:0.9e}".format(x1), "{0:0.9e}".format(fx1), error])
                elif x1 != 0 and fx1 != 0 and error != 0:
                    ansTable.append([cont, "{0:0.9e}".format(x1), "{0:0.9e}".format(fx1), "{0:0.2e}".format(error)])
                else:
                    ansTable.append([cont, x1, fx1, error])

            if fx1 == 0:
                return ansTable, f"{x1} is the root"

            elif error < tol:
                return ansTable, f"{x1} is an approximation to a root with a tolerance = {tol} and after {niter} iterations"
            elif den == 0:
                return ansTable, f"There is a possible multiple root"
            else:
                return ansTable, f"Failed after {niter} iterations"


#sec = Secant()
#print(sec.evaluate(1E-7, 0.5, 1, fc.f, 100))