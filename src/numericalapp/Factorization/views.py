from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
import numpy as np

from .methods.lusimple import LU_simple

# Create your views here.
class Matrix(forms.Form):
    rows = forms.IntegerField(min_value=2, max_value=8)

class Matrix2(forms.Form):
    iter = forms.IntegerField(min_value=1, max_value=100)
    tol = forms.FloatField(required=True)
    rel = forms.FloatField(required=True)

class MatrixElement(forms.Form):
    element = forms.FloatField(label=False, widget=forms.NumberInput(attrs={'size': '5'}))
    element: {'widget': forms.NumberInput(attrs={'class':'form-number'})}


def LUSimple_view(request):
    message = ''
    stages = []
    matrixs = []
    xs = []
    ab = []
    a = []
    x = []
    A = []
    L =[]
    U =[]
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
            # print(f" A {A} \n b {b}")
            message, A, L, U, x, a = LU_simple(matrix,request.session['matrix_size'])
            print("message", message)

    # print(request.session['matrix_size'])
    # print(matrixs)
    print(f"A {A}, \n L {L} \n U \n x {x}")
    print("a",a)    
        
    return render(request, 'methods/factorization/lusimple.html', { "A": A, "L": L, "U":U,
        "size":request.session['matrix_size'], "form": Matrix(), "element": MatrixElement(), "message": message, "x":x, "sol": a,
    })

