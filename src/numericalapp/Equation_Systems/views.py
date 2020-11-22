from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def doolittle_view(request, *args, **kwargs):
    return render(request, 'methods/equation_systems/doolittle.html',{})

def gaussSeidel_view(request, *args, **kwargs):
    return render(request, 'methods/equation_systems/gaussSeidel.html',{})

def jacobi_view(request, *args, **kwargs):
    return render(request, 'methods/equation_systems/jacobi.html',{})