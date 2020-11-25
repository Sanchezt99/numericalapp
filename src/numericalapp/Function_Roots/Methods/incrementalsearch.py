
from math import *


def Incrementalsearches(function,initialvalue,delta,iterations):
   print(function,initialvalue,delta,iterations)
   f=function
   xo=initialvalue     
   d=delta
   i=iterations
   message = ""
   ansTable = []

   def func():
       x=xo
       res = eval(f)
       return float(res)
      
   def fun1():
       x=xa
       res = eval(f)
       return res

   if func() == 0.0:
       message = str(x) + " is root"
       return message, ansTable


   else:
       if message:
           print("message")
           return message

       cont = 1 
       encontrado=False
       while (cont < i):
           res1 = func()
           xa = xo + d
           res2 = fun1()
           if res2 == 0:
               message = str(xa) + " is root"
               return message, []
               print (xa,"is root")
           else:
               if (res1*res2 < 0):
                   m = "There is a root of f in [","{:14.10f}".format(xo),",","{:14.10f}".format(xa),"]"
                   ansTable.append(m)
                   encontrado=True
           cont = cont + 1
           xo=xa
   if ((cont==i) and (not encontrado)):
       message = "With the number of requested iterations, no interval was found that could contain a root"
       print("With the number of requested iterations, no interval was found that could contain a root")
       
       return message, ansTable
Incrementalsearches('log(sin(x)**2+1)-1/2', -3, 0.5, 100)

