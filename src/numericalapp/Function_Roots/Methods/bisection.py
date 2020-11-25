from math import *
    
def Bisection(limitlower,upperanger,funtion,iterations,tolerance):
   a=limitlower
   b=upperanger
   f=funtion
   i=iterations
   tol=tolerance
   control = 1
   message = ""
   ansTable = []
   x = 0

   def fun1():
        print("F",f)
        x = a
        ya = eval(f)
        return ya
    
   def fun2():
            x = b
            yb = eval(f)
            return yb
    
   def funm():
            x = c
            yc = eval(f)
            return yc

   if fun1 == 0:
        message = str(a) + " is root"
   else:
        if fun2==0:
            message = str(b) + " is root"
        else:
            if (fun1()*fun2())>0:
                message = "inappropriate interval"
        
            if message:
                    return message, [], 0
            else:
                c = (a+b)/2
                funm()
                error = tol + 1
                cont = 1
                while (funm()!= 0)&(error>tol)&(cont<i):
                    if control == 1:
                            ansTable.append([str(cont), str(a), str(c), str(b), str(funm()), ' '])
                            print ("| iter  |        a       |","      xm       |","       b       |","  f(Xm)  |","   E    |")
                            print ("|","{:5.0f}".format(cont),"|","{:14.10f}".format(a),"|","{:14.10f}".format(c),"|","{:14.10f}".format(b),"|","{:0.1e}".format(funm()),"|         |")
                            cont=cont+1
                    control=2

                    if (fun1()*funm())<0:
                            b = c
                            fun2()
    
                    else:
                            a = c
                            fun1()
    
                    xaux=c
    
                    float(c)
                    c = ((a+b)/2)
                    fm=funm()
                    float(error)
                    error = abs(c-xaux)
                    print ("|","{:5.0f}".format(cont),"|","{:14.10f}".format(a),"|","{:14.10f}".format(c),"|","{:14.10f}".format(b),"|","{:0.1e}".format(fm),"|","{:0.1e}".format(error),"|")
                    ansTable.append([str(cont), str(a), str(c), str(b), str(fm), str(error)])
                    cont = cont + 1
                if funm() == 0:
                        print ("\n\n",c,"is root")
                        x = c
                else:
                        if error < tol:
                                x = c
                                print ("\n\nSe encontró una aproximación de la raiz en ","{:18.15f}".format(c))
                        else:
                                message = "failed"
                                print ("failed")

        return message, ansTable, x
                                