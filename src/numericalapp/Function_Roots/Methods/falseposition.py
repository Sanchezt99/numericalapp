from math import sin
import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr as pe

def FalseRule(f,x1,x2,tol,maxfpos):
        xh = 0
        matrixh = []
        matrixa = []
        matrixb = []
        matrixfxh = []
        message = ""
        fpos = 0
        f = pe(f)
        x = sp.symbols('x')



        if x1>=x2:
                message = "a has to be smaller than b"
                return message,None,None,None,None
        try:
                f.subs(x,x1)
                f.subs(x,x2)
                
        except:
                message= ""
                return message,None,None,None,None
        if str(f.subs(x,x1)) == 'zoo' or str(f.subs(x,x2)) == 'zoo' : 
                message = "Undefined function for the intervals"
                return message,None,None,None,None

        fx1 = f.subs(x,x1)
        fx2 = f.subs(x,x2)
        if 'I' in str(f.subs(x,x1)) or  str(f.subs(x,x2)):
                message ="The initial value must be in the function domain"
                return message,None,None,None,None
        if fx1 * fx2 < 0:
                for fpos in range(1,maxfpos+1):
        

                        xh = x2 - (x2-x1)/(fx2-fx1) *fx2
                        matrixh.append(xh)
                        matrixa.append(x1)
                        matrixb.append(x2)
                        message = "The root is " + str(xh)
                        fxh = f.subs(x,xh)
                        matrixfxh.append(fxh)
                        if abs(fxh) < tol:
                                break
                        elif fx1 * fxh< 0:
                                x2 = xh
                        else:
                                x1 = xh
        else:
                message =("no root in the intervals")
        return message,matrixh,matrixa,matrixb,matrixfxh

#def funcs and vars