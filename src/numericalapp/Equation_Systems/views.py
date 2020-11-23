from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .Methods.gaussSimple import gauss_enter, gauss_elimination
# Create your views here.


matrix = []

class Matrix(forms.Form):
    rows = forms.IntegerField(min_value=2, max_value=8)

class MatrixElement(forms.Form):
    element = forms.FloatField(label=False)



def doolittle_view(request, *args, **kwargs):
    return render(request, 'methods/equation_systems/doolittle.html',{})

def gaussSeidel_view(request, *args, **kwargs):
    return render(request, 'methods/equation_systems/gaussSeidel.html',{})

def jacobi_view(request, *args, **kwargs):
    return render(request, 'methods/equation_systems/jacobi.html',{})

def methods(request):
    return render(request, "methods.html")

def graph(request):
    return render(request, "graph.html")


def gaussSimple_view(request):
    message = ''
    stages = []
    matrixs = []
    if 'matrix_size' not in request.session:
        request.session['matrix_size'] = 2
        
    if request.method == "POST":
        if "rows_matrix" in request.POST:
            form = Matrix(request.POST)
            if form.is_valid():
                row = form.cleaned_data["rows"]
                request.session['matrix_size'] = row

        if "method" in request.POST:
            elements = request.POST.getlist('element')
            
            matrix = elements
            A,b = gauss_enter(matrix,request.session['matrix_size'])
            print(f" A {A} \n b {b}")
            message, stages, matrixs = gauss_elimination(A,b)
            print("message", message)

    print(request.session['matrix_size'])
    print(matrixs)
    return render(request, 'methods/equation_systems/gauss.html', {
            "size":request.session['matrix_size'], "form": Matrix(), "element": MatrixElement(), "message": message, "stages":stages, "matrixs": matrixs
    })


