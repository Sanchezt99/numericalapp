from math import *

def FalseRule(limitlower,upperanger,funtion,iterations,tolerance):
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
        print (a,"is root")
   else:
        if fun2==0:
            message = str(b) + " is root"
        else:
            if (fun1()*fun2())>0:
                message = "inappropriate interval"
                print ("inappropriate interval")
            else:
                if message:
                        return message, [], x
                    
                c = a-((fun1()*(b-a))/(fun2()-fun1()))
                funm()
                error = tol + 1
                cont = 1
                while (funm()!= 0)&(error>tol)&(cont<i):
                    if (fun1()*funm())<0:
                            b = c
                            fun2()
    
                    else:
                            a = c
                            fun1()
    
                    xaux=c
                    if control == 1:
                            print ("| iter  |        a       |","      xm       |","       b       |","     f(Xm)     |","      E        |")
                    control=2
    
                    float(c)
                    c = a-((fun1()*(b-a))/(fun2()-fun1()))
                    fm=funm()
                    float(error)
                    error = abs(c-xaux)
                    print ("|","{:5.1f}".format(cont),"|","{:14.11f}".format(a),"|","{:14.11f}".format(c),"|","{:14.11f}".format(b),"|","{:14.11f}".format(fm),"|","{:14.11f}".format(error),"|")
                    ansTable.append([str(cont), str(a), str(c), str(b), str(fm), str(error)])
                    cont = cont + 1
                if funm() == 0:
                        print ("\n\n",c,"is root")
                        x = c
                else:
                        if error < tol:
                                print ("\n\n",c,"is root with tol:",error)
                                x = c
                        else:
                                print ("failure")
                                message = "failure"
                
                return message, ansTable, x
                                
                                
                                
                                                                                              
FalseRule(0,1,'log(sin(x)**2+1)-1/2',100,0.0000001)