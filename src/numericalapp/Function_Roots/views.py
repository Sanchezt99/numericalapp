from django.shortcuts import render
from django.http import HttpResponse
from .Forms import *
from .Methods import FixedPoint
#  x0, tolerancia, iter, function, g_function, type_error=0

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
        print(res)
        return render(request, 'methods/function_roots/fixedPoint.html',{'form':form,'res':res,'sol':sol})
    else:
        form = FixedPointForm()
        return render(request, 'methods/function_roots/fixedPoint.html',{'form':form})

def secant_view(request, *args, **kwargs):
    return render(request, 'methods/function_roots/secant.html',{})

def newton_view(request, *args, **kwargs):
    return render(request, 'methods/function_roots/newton.html',{})