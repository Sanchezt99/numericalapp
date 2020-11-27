import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr as pe


def bisection(a,b, f, tol,i):
        f = pe(f)
        x = sp.symbols('x')

        xl = a
        xr = b
        counter = 0
        c= 0
        x = sp.symbols('x')
        message = ""
        arra = []
        arrb = []
        arre = []
        arrxm = []
        arrfxm = []
        if a>b:
                message = "a has to be smaller than b"
                return None,None,None,None,None,message
        try:
                f.subs(x,xl)
                f.subs(x,xr)
                
        except:
                message= ""
                return None,None,None,None,None,message

        while (np.abs(xl-xr)>= tol):
                # print(f)
                if counter > i:
                        message = "no root found after", counter, "iterations, only got to", c 
                        return None,None,None,None,None,message
                if counter > 2:
                        aux = c
                c =(xl + xr)/2.0
                arrxm.append(c)
                arre.append(np.abs(xl-xr))
                arra.append(xl)
                arrb.append(xr)
                arrfxm.append(f.subs(x,c))
                fxl = f.subs(x,xl)
                fxc = f.subs(x,c)
                print(c)
                prod = fxl*fxc

                if prod > tol:
                        xl = c
                else:
                        if prod< tol:
                                xr = c
                counter= counter +1
        return arra, arrb, arre, arrxm, arrfxm, message