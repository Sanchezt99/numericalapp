import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr as pe
from scitools.StringFunction import StringFunction
from math import *

class Newton:
    def __init__(self):
        self.values = []

    def evaluate(self, tol, xi, niter, fun, dfun, type_error=0):
        
        ansTable = [] 
        ansTable.append(["i", "xi", "f(xi)", "E"])
        x = sp.symbols('x')
        function = pe(fun)
        dfunction = pe(dfun)
        fx = function.subs(x,xi)
        dfx = dfunction.subs(x,xi) 

        if fx == 0:
            return ansTable, str(fx) + " is a root."
        if dfun == 0:
            return "The derivate can't be 0"

        counter = 0
        error = tol + 1

        self.values.append([counter, str(xi), str(
            "{:.2e}".format(fx)), str(dfx), None])


        xn = 0
        while error > tol and fx != 0 and dfx != 0 and counter - 1 < niter:
            xn = xi - (fx.subs(x,xi)/dfx.subs(x,xi))
            fx = function.subs(x,xn)
            dfx = dfunction.subs(x,xn)
            ansTable.append([counter, "{0:0.9e}".format(xi), "{0:0.9e}".format(fx), "{0:0.2e}".format(error)])
            #print(counter, xi, fun(xi),error)

            if type_error == 0:
                error = abs(xn-xi)
            else:
                error = abs((xn-xi)/xn)

            xi = xn

            counter = counter + 1
            #self.values.append([counter, str(xn), str("{:.2e}".format(fx)), str(dfx), str("{:.2e}".format(error))])
        ansTable.append([counter, "{0:0.9e}".format(xi), "{0:0.9e}".format(fx), "{0:0.2e}".format(error)])
        if fx == 0:
            ansTable.append(xi)
            #return f"{xi} is a root"
            return ansTable , xi
            
        elif error < tol:
            #return f"{xi} its an aproximation to a root with a tolerance of {tol}"
            return ansTable , f'The root is an approximation of {xi} with a tolerance of {tol}'
        elif dfx == 0:
            return ansTable, f"{xi} Possible multiple root"
        else:
            return ansTable, f"Failed after {niter} iterations"

    def tabla_values(self):
        return self.values

newt = Newton()
#print(newt.evaluate(0.00001,1,100,fc.fPrime,fc.fPrimePrime))

