import sympy as sp
from sympy.core.numbers import ImaginaryUnit
from sympy.parsing.sympy_parser import parse_expr as pe
from math import *
import numpy as np

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
        if 'I' in str(fx):
            return ansTable, " I can't compute imaginary numbers such as :" + str(fx)
        if 'I' in str(dfx):
            return ansTable," I can't compute imaginary numbers such as :" + str(dfx)
        if fx == 0:
            return ansTable, str(fx) + " is a root."
        if dfun == 0:
            return ansTable, "The derivate can't be 0"

        counter = 0
        error = tol + 1

        xn = 0
        while not isinstance(fx, sp.core.numbers.ComplexInfinity) and not isinstance(xn, sp.core.numbers.ComplexInfinity) and not isinstance(dfx,sp.core.numbers.ComplexInfinity) and error > tol and fx != 0 and dfx != 0 and counter - 1 < niter:    
            xn = xi - (fx.subs(x,xi)/dfx.subs(x,xi))

            fx = function.subs(x,xn)
            dfx = dfunction.subs(x,xn) 
            ansTable.append([counter, xi, fx, error])
            #print(counter, xi, fun(xi),error)

            if type_error == 0:
                error = abs(xn-xi)
            else:
                error = abs((xn-xi)/xn)
            
            xi = xn
            # print(xn)
            counter = counter + 1
            
        
        if isinstance(dfx, sp.core.numbers.ComplexInfinity) and isinstance(fx, sp.core.numbers.ComplexInfinity):
            print("4")
            return ansTable , f'Check both functions f(x) = {function} and f\'(x) = {dfunction} continuity'
        elif isinstance(dfx, sp.core.numbers.ComplexInfinity):
            return ansTable , f'Check function f\'(x) = {dfunction} continuity'
            print(5)
        elif isinstance(fx, sp.core.numbers.ComplexInfinity):
            print(6)
            return ansTable , f'Check function f(x) = {function} continuity'
        
        elif xi != 0 and fx != 0 and error != 0:
            print(7)
            ansTable.append([counter, "{0:0.9e}".format(xi), "{0:0.9e}".format(fx), "{0:0.2e}".format(error)])
        elif xi == 0 and fx != 0 and error != 0:
            print("8")
            ansTable.append([counter, xi, "{0:0.9e}".format(fx), "{0:0.2e}".format(error)])
        elif counter != 0 and xi == 0 and fx != 0 and error != 0:
            print("9")
            ansTable.append([counter, "{0:0.9e}".format(xi), fx, "{0:0.2e}".format(error)])
        elif counter != 0 and xi != 0 and fx != 0 and error == 0:
            print("10")
            ansTable.append([counter, "{0:0.9e}".format(xi), "{0:0.9e}".format(fx), error])
        else: 
            print("11")
            ansTable.append([counter, xi, fx, error])


        if fx == 0:
            print(12)
            #ansTable.append(xi)
            #return f"{xi} is a root"
            return ansTable , xi
            
        elif error < tol:
            print(13)
            #return f"{xi} its an aproximation to a root with a tolerance of {tol}"
            return ansTable , f'The root is an approximation of {xi} with a tolerance of {tol}'
        elif dfx == 0:
            print(14)
            return ansTable, f"{xi} Possible multiple root"
        else:
            print(15)
            return ansTable, f"Failed after {niter} iterations"

  


newt = Newton()
#print(newt.evaluate(0.00001,1,100,fc.fPrime,fc.fPrimePrime))

