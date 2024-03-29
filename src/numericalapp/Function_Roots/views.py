from django.shortcuts import render
from django.http import HttpResponse
from .Forms import *
from .Methods import FixedPoint,Secant,newton,falseposition,bisection
from .Methods.multipleRoots import multiple_roots
from .Methods.bisection import bisection
from .Methods.falseposition import FalseRule
from .Methods.incrementalsearch import Incrementalsearches


def fixedPoint_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = FixedPointForm(request.POST)
        fp = FixedPoint.FixedPoint()
        x0 = float(form.data['x0'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])
        F = form.data['F']
        G = form.data['G']


        res,sol = fp.evaluate(x0,Tol,Iter,F,G)
        #print(res)
        return render(request, 'methods/function_roots/fixedPoint.html',{'form':form,'res':res,'sol':sol})
    else:
        form = FixedPointForm()
        return render(request, 'methods/function_roots/fixedPoint.html',{'form':form})

def newton_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = NewtonForm(request.POST)
        newt = newton.Newton()
        xi = float(form.data['xi'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])
        Fu = form.data['F']
        FPrime = form.data['FPrime']


        res,sol = newt.evaluate(Tol,xi,Iter,Fu,FPrime)
        #print(res)
        return render(request, 'methods/function_roots/newton.html',{'form':form,'res':res,'sol':sol})
    else:
        form = NewtonForm()
    return render(request, 'methods/function_roots/newton.html', {'form':form})

def secant_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = SecantForm(request.POST)
        sec = Secant.Secant()
        x0 = float(form.data['x0'])
        x1 = float(form.data['x1'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])
        F = form.data['F']
        res,sol = sec.evaluate(Tol,x0,x1,F,Iter)
        return render(request, 'methods/function_roots/secant.html',{'form':form,'res':res,'sol':sol})
    else:
        form = SecantForm()
    return render(request, 'methods/function_roots/secant.html', {'form':form})

def multipleRoots_view(request):
    if request.method == 'POST':
        form = MultipleRootsForm(request.POST)
        F = form.data['F']
        FP = form.data['FP']
        F2P = form.data['F2P']

        x0 = float(form.data['x0'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])

        res, sol = multiple_roots(F,FP, F2P ,Tol,Iter,x0)
        return render(request, 'methods/function_roots/multipleRoots.html',{'form':form,'res':res,'sol':sol})
    else:
        form = MultipleRootsForm()
    return render(request, 'methods/function_roots/multipleRoots.html', {'form':form})

def incrementalsearch_view(request, *args, **kwargs):
    message = ""
    ansTable = []

    if request.method == 'POST':
        form = incrementalsearchForm(request.POST)
        x0 = float(form.data['x0'])
        Delta = float(form.data['Delta'])
        Iter = int(form.data['Iter'])
        F = form.data['F']
        ansTable, message = Incrementalsearches(F,x0,Delta,Iter )
        return render(request, 'methods/function_roots/incrementalsearch.html',{'form':form,'message':message,'res':ansTable})
    else:
        form = incrementalsearchForm()
    return render(request, 'methods/function_roots/incrementalsearch.html', {'form':form})

def bisection_view(request, *args, **kwargs):
    message = ""
    arra = []
    arrb = []
    arre = []
    arrxm = []
    arrfxm = []

    if request.method == 'POST':
        form = bisectionForm(request.POST)
        a = float(form.data['a'])
        b = float(form.data['b'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])
        F = form.data['F']

        arra, arrb, arre, arrxm, arrfxm, message = bisection(a,b,F,Tol,Iter)

        return render(request, 'methods/function_roots/bisection.html',{'form':form,'message':message,'arra':arra, 'arrxm':arrxm,'arrb':arrb, 'arre':arre, 'arrfxm':arrfxm})
    else:
        form = bisectionForm()
    return render(request, 'methods/function_roots/bisection.html', {'form':form})



def falseposition_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = falsepositionForm(request.POST)
        a = float(form.data['a'])
        b = float(form.data['b'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])
        F = form.data['F']
        message,matrixh,matrixa,matrixb,matrixfxh = FalseRule(F,a,b,Tol,Iter)
        return render(request, 'methods/function_roots/falseposition.html',{'form':form,'message':message,'matrixa':matrixa, 'matrixb':matrixb,'matrixh':matrixh,'matrixfxh':matrixfxh})
    else:
        form = falsepositionForm()
    return render(request, 'methods/function_roots/falseposition.html', {'form':form})
