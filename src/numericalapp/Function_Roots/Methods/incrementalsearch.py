from sympy.parsing.sympy_parser import parse_expr as pe
import sympy as sp
from math import *


def Incrementalsearches(function,initialvalue,delta,iterations):
   f= pe(function)
   xo=initialvalue     
   d=delta
   i=iterations
   message = ""
   ansTable = []
   x = sp.symbols('x')

   if f.subs(x,xo) == 0.0:
       message = str(x) + " is root"
       return message, ansTable


   else:

       cont = 1 
       encontrado=False
       while (cont < i):
           res1 = f.subs(x,xo)
           xa = xo + d
           res2 = f.subs(x,xa)
           if res2 == 0:
               message = str(xa) + " is root"
               return message, ansTable
           else:
               if (res1*res2 < 0):
                   m = "There is a root of f in [","{:14.10f}".format(xo),",","{:14.10f}".format(xa),"]"
                   ansTable.append(m)
                   encontrado=True
           cont = cont + 1
           xo=xa
   if ((cont==i) and (not encontrado)):
       message = "With the number of requested iterations, no interval was found that could contain a root"
       
       return message, ansTable

