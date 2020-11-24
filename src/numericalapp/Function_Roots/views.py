from django.shortcuts import render
from django.http import HttpResponse
from .Forms import *
from .Methods import FixedPoint,Secant,Newton,incrementalsearch,falseposition,bisection


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
        newt = Newton.Newton()
        xi = float(form.data['xi'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])
        F = form.data['F']
        FPrime = form.data['FPrime']


        res,sol = newt.evaluate(Tol,xi,Iter,F,FPrime)
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
        #print(res)
        return render(request, 'methods/function_roots/secant.html',{'form':form,'res':res,'sol':sol})
    else:
        form = SecantForm()
    return render(request, 'methods/function_roots/secant.html', {'form':form})

def incrementalsearch_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = incrementalsearchForm(request.POST)
        inc = incrementalsearch.incrementalsearch()
        x0 = float(form.data['x0'])
        Delta = float(form.data['Delta'])
        Iter = int(form.data['Iter'])
        F = form.data['F']
        res,sol = inc.evaluate(Tol,x0,Delta,F,Iter)
        #print(res)
        return render(request, 'methods/function_roots/incrementalsearch.html',{'form':form,'res':res,'sol':sol})
    else:
        form = incrementalsearchForm()
    return render(request, 'methods/function_roots/incrementalsearch.html', {'form':form})

def bisection_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = bisectionForm(request.POST)
        bisc = bisection.bisection()
        a = float(form.data['a'])
        b = float(form.data['b'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])
        F = form.data['F']
        res,sol = bisc.evaluate(Tol,a,b,F,Iter)
        #print(res)
        return render(request, 'methods/function_roots/bisection.html',{'form':form,'res':res,'sol':sol})
    else:
        form = bisectionForm()
    return render(request, 'methods/function_roots/bisection.html', {'form':form})

def falseposition_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = falsepositionForm(request.POST)
        fals = falseposition.falseposition()
        a = float(form.data['a'])
        b = float(form.data['b'])
        Tol = float(form.data['Tol'])
        Iter = int(form.data['Iter'])
        F = form.data['F']
        res,sol = fals.evaluate(Tol,a,b,F,Iter)
        #print(res)
        return render(request, 'methods/function_roots/falseposition.html',{'form':form,'res':res,'sol':sol})
    else:
        form = falsepositionForm()
    return render(request, 'methods/function_roots/falseposition.html', {'form':form})