from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fixedPoint_view(request, *args, **kwargs):
    return render(request, 'methods/function_roots/fixedPoint.html',{})

def secant_view(request, *args, **kwargs):
    return render(request, 'methods/function_roots/secant.html',{})

def newton_view(request, *args, **kwargs):
    return render(request, 'methods/function_roots/newton.html',{})