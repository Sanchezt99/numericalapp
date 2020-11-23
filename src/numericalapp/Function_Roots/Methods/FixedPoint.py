import math, os, sys
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr as pe
from scitools.StringFunction import StringFunction
import utils.Functions as fc


class FixedPoint:

    def __init__(self):
        self.values = []

    def evaluate(self, x0, tol, iter, f, g, type_error=0):
        ansTable = [] 
        ansTable.append(["i", "xi", "g(xi)", "f(xi)", "E"])

        x = sp.symbols('x')
        function = pe(f)
        g_function = pe(g)
        fx = function.subs(x,x0)

        if fx == 0:
            print(f"{x0} is the root")
            return f"{x0} is the root"
        if iter < 1:
            print("The iterator value is wrong")
            return "The iterator value is wrong"
        if tol < 0:
            print("Tolerance error, must be greater than or equal to 0")
            return "Tolerance error, must be greater than or equal to 0"

        self.values.append([0, str(x0), str(fx), None])
        counter = 0
        error = tol + 0.1
        while fx != 0 and error > tol and counter < iter:
            xn = g_function.subs(x,x0)
            fi = function.subs(x,xn)
            fn = function.subs(x,x0)
            ansTable.append([counter, "{0:0.9e}".format(x0), "{0:0.9e}".format(xn), "{0:0.9e}".format(fn), "{0:0.9e}".format(error)])
            if type_error == 0:
                error = abs(xn-x0)
            else:
                error = abs((xn-x0)/xn)

            x0 = xn

            counter = counter + 1

            self.values.append([counter, str(xn), str(fi), str(error)])
        

        if fx == 0:
            ansTable.append(x0)
            return ansTable
        elif error < tol:
            #ansTable.append([x0,tol,counter])
            return ansTable , f'The root is an approximation of: {x0} with a tolerance of {tol}'
        else:
            return f"Failed after {iter} iterations "

    def tabla_values(self):
        print(self.values)
        return self.values
