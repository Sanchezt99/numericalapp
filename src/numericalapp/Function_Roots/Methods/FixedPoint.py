import math
from scitools.StringFunction import StringFunction
from math import *
import utils.Funcions as fc

class FixedPoint:

    def __init__(self):
        self.values = []

    def evaluate(self, x0, tolerancia, iter, function, g_function, type_error=0):

        print("iter", "xi", "g(xi)", "f(xi)", "E")

        fx = function(x0)

        if fx == 0:
            print(f"{x0} is the root")
            return f"{x0} is the root"
        if iter < 1:
            print("The iterator value is wrong")
            return "The iterator value is wrong"
        if tolerancia < 0:
            print("Tolerance error, must be greater than or equal to 0")
            return "Tolerance error, must be greater than or equal to 0"

        self.values.append([0, str(x0), str("{:.2e}".format(fx)), None])
        contador = 0
        error = tolerancia + 0.1
        while fx != 0 and error > tolerancia and contador < iter:
            xn = g_function(x0)
            fi = function(xn)
            fn = function(x0)
            print(contador, x0, xn, fn, error)

            if type_error == 0:
                error = abs(xn-x0)
            else:
                error = abs((xn-x0)/xn)

            x0 = xn

            contador = contador + 1

            self.values.append([contador, str(xn), str(
                "{:.2e}".format(fi)), str("{:.2e}".format(error))])


        if fx == 0:
            return f"{x0} is the root"
        elif error < tolerancia:
            return f"{x0} is an aproximation with tolerance of {tolerancia} and after {contador} iterations"
        else:
            return f"Failed after {iter} iterations "

    def tabla_values(self):
        print(self.values)
        return self.values

fpoint = FixedPoint()
print(fpoint.evaluate(-0.5, 1E-7, 100, fc.f, fc.e))