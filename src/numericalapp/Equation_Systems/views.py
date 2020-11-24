from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from numpy.lib.function_base import append

from .Methods.Doolittle import *
from .Methods.Gauss_Seidel import *
from .Methods.Jacobi import *
from .Methods.gaussSimple import gauss_enter, gauss_elimination
import numpy as np
# Create your views here.


matrix = []

class Matrix(forms.Form):
    rows = forms.IntegerField(min_value=2, max_value=8)

class Matrix2(forms.Form):
    iter = forms.IntegerField(min_value=1, max_value=100)
    tol = forms.FloatField(required=True)
    rel = forms.FloatField(required=True)


class MatrixElement(forms.Form):
    element = forms.FloatField(label=False, widget=forms.NumberInput(attrs={'size': '5'}))
    element: {'widget': forms.NumberInput(attrs={'class':'form-number'})}



def doolittle_view(request, *args, **kwargs):
    message = ''

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
            
            n = request.session['matrix_size'] * request.session['matrix_size']
            n2= request.session['matrix_size']
            elementsa = elements[:n]
            elementsb = elements[n:]
            print(elementsa)
            print(elementsb)
            
            matriEntr = np.zeros( (n2, n2) )
            matriEntr2 = np.zeros( (1, n2) )
            for i in range(0,len(elementsb)):
                for j in range(0,len(elementsb)):
                    matriEntr[i][j] = elementsa[(i*n2) + j]
   
            for j in range(0,len(elementsb)):
                matriEntr2[0][j] = elementsb[j]

            # print(matriEntr)
            matrixs = Doolittle.evaluate(matriEntr,len(elementsb),matriEntr2)
    #         print(matrixs)
    #         print("message", message)

    # print(request.session['matrix_size'])
    print(matrixs)
    
    return render(request, 'methods/equation_systems/doolittle.html', {
            "size":request.session['matrix_size'], "form": Matrix(), "element": MatrixElement(),"elementb": MatrixElement(), "matrixs": matrixs
    })


def gaussSeidel_view(request, *args, **kwargs):
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
            form2 = Matrix2(request.POST)
            if form2.is_valid():
                Tol = form2.cleaned_data["tol"]
                Iter = form2.cleaned_data["iter"]
                rel = form2.cleaned_data["rel"]

            # variables
            
            n = request.session['matrix_size'] * request.session['matrix_size']
            n2= request.session['matrix_size']
            n3 = request.session['matrix_size'] * request.session['matrix_size'] +n2
            elementsa = elements[:n]
            elementsb = elements[n:]
            elementsx0 = elements[n3:]
            matrixa = np.zeros( (n2, n2) )
            matrixb = np.zeros( (1, n2) )
            matrixx0 = np.zeros( (1, n2) )
            for i in range(0,n2):
                for j in range(0,n2):
                    matrixa[i][j] = elementsa[(i*n2) + j]
                    
            for j in range(0,n2):
                matrixb[0][j] = elementsb[j]

            for j in range(0,n2):
                matrixx0[0][j] = elementsx0[j]

            # print(f" A {A} \n b {b}")
            matrixs = GaussSeidel.evaluate(Tol,Iter,rel,matrixa,n2,matrixb,matrixx0)
            # print("message", message)
            print(matrixs)
    # print(request.session['matrix_size'])
    # print(matrixs)
    return render(request, 'methods/equation_systems/gaussSeidel.html', {
            "size":request.session['matrix_size'], "form2":Matrix2(),"form": Matrix(), "element": MatrixElement(), "message": message, "stages":stages, "matrixs": matrixs
    })

def jacobi_view(request, *args, **kwargs):
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
            form2 = Matrix2(request.POST)
            if form2.is_valid():
                Tol = form2.cleaned_data["tol"]
                Iter = form2.cleaned_data["iter"]
                rel = form2.cleaned_data["rel"]

            # variables
            
            n = request.session['matrix_size'] * request.session['matrix_size']
            n2= request.session['matrix_size']
            n3 = request.session['matrix_size'] * request.session['matrix_size'] +n2
            elementsa = elements[:n]
            elementsb = elements[n:]
            elementsx0 = elements[n3:]
            matrixa = np.zeros( (n2, n2) )
            matrixb = np.zeros( (1, n2) )
            matrixx0 = np.zeros( (1, n2) )
            for i in range(0,n2):
                for j in range(0,n2):
                    matrixa[i][j] = elementsa[(i*n2) + j]
                    
            for j in range(0,n2):
                matrixb[0][j] = elementsb[j]

            for j in range(0,n2):
                matrixx0[0][j] = elementsx0[j]

            # print(f" A {A} \n b {b}")
            matrixs = Jacobi.evaluate(Tol,Iter,rel,matrixa,n2,matrixb,matrixx0)
            # print("message", message)
            print(matrixs)
    # print(request.session['matrix_size'])
    # print(matrixs)
    return render(request, 'methods/equation_systems/jacobi.html', {
            "size":request.session['matrix_size'], "form2":Matrix2(),"form": Matrix(), "element": MatrixElement(), "message": message, "stages":stages, "matrixs": matrixs
    })

def methods(request):
    return render(request, "methods.html")

def graph(request):
    return render(request, "graph.html")


matrix_final = []
def gaussSimple_view(request):
    message = ''
    stages = []
    matrixs = []
    xs = []
    ab = []
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
            # print(f" A {A} \n b {b}")
            message, matrixs, xs, ab = gauss_elimination(A,b)
            print("message", message)

    # print(request.session['matrix_size'])
    # print(matrixs)
    print(request.session['matrix_final'])
    return render(request, 'methods/equation_systems/gauss.html', {
         "m":ab, "size":request.session['matrix_size'], "form": Matrix(), "element": MatrixElement(), "message": message, "matrixs": matrixs, "xs":xs
    })

