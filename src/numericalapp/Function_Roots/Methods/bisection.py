import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr as pe


def bisection(a,b, f, tol,i):
        f = pe(f)
        x = sp.symbols('x')
        print(f.subs(x,b))
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
        if a > 0:
                message = "There is not root for the intervals "
                return None,None,None,None,None,message
        if 'I' in str(f.subs(x,xl)) or  str(f.subs(x,xr)):
                message ="The initial value must be in the function domain"
                return None,None,None,None,None,message
        if a>=b:
                message = "a has to be smaller than b"
                return None,None,None,None,None,message
        try:
                f.subs(x,xl)
                f.subs(x,xr)
                
        except:
                message= ""
                return None,None,None,None,None,message
        if str(f.subs(x,xl)) == 'zoo' or str(f.subs(x,xr)) == 'zoo' : 
                message = "Undefined function for the intervals"
                return None,None,None,None,None,message
        while (np.abs(xl-xr)>= tol):
                # print(f)
                if counter > i:
                        message = "no root found after", counter, "iterations, only got to", c 
                        return None,None,None,None,None,message
                if counter > 2:
                        aux = c
                c =(xl + xr)/2.0
                arrxm.append(format(c,",.3e"))
                arre.append(format(np.abs(xl-xr),",.3e"))
                arra.append(format(xl,",.3e"))
                arrb.append(format(xr,",.3e"))
                arrfxm.append(format(f.subs(x,c),",.3e"))
                fxl = f.subs(x,xl)
                fxc = f.subs(x,c)
     
                prod = fxl*fxc

                if prod > tol:
                        xl = c
                else:
                        if prod< tol:
                                xr = c
                counter= counter +1
        message = "The root is " + str(c)
        return arra, arrb, arre, arrxm, arrfxm, message