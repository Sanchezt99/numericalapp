from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from numpy.lib.function_base import append
from numpy.linalg.linalg import solve

from .Methods.Doolittle import *
from .Methods.Gauss_Seidel import *
from .Methods.Jacobi import *
from .Methods.gaussSimple import gauss_enter, gauss_elimination


from .Methods import partial_pivot, total_pivot



import numpy as np
# Create your views here.


matrix = []
matrix12=[]
class Matrix(forms.Form):
    rows = forms.IntegerField(min_value=2, max_value=8,)

class Matrix2(forms.Form):
    iter = forms.IntegerField(min_value=1, max_value=100)
    tol = forms.FloatField(required=True, min_value=1e-15)



class MatrixElement(forms.Form):
    element = forms.FloatField(label=False, widget=forms.NumberInput(attrs={'size': '5'}),initial=1)
  



def doolittle_view(request, *args, **kwargs):
    message = ''
    matrixs = []
    ans=[]
    matriEntr = []
    matriEntr2 = []
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
            matriEntr = np.zeros( (n2, n2) )
            matriEntr2 = np.zeros( (1, n2) )
            for i in range(0,len(elementsb)):
                for j in range(0,len(elementsb)):
                    matriEntr[i][j] = elementsa[(i*n2) + j]
   
            for j in range(0,len(elementsb)):
                matriEntr2[0][j] = elementsb[j]

            print(matriEntr[0][1])
            matrixs,ans,message = Doolittle.evaluate(matriEntr,len(elementsb),matriEntr2)
            matrix12 = elementsa

    
    return render(request, 'methods/equation_systems/doolittle.html', {
            "size":request.session['matrix_size'], "form": Matrix(),"size":request.session['matrix_size'],'matrix1': matriEntr,'matrix2':matriEntr2,'message':message ,'ans':ans,"element": MatrixElement(),"elementb": MatrixElement(), "matrixs": matrixs
    })


def gaussSeidel_view(request, *args, **kwargs):
    message = ''
    stages = []
    matrixs = []
    matrixa=[]
    matrixb=[]
    error = []
    matrixx0=[]
    T=[]
    C=[]
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


            # variables
            
            n = request.session['matrix_size'] * request.session['matrix_size']
            n2= request.session['matrix_size']
            n3 = request.session['matrix_size'] * request.session['matrix_size'] +n2
            elementsa = elements[:n]
            elementsb = elements[n:]
            elementsx0 = elements[n3:]
            matrixa = np.zeros( (n2, n2) )
            matrixb = np.zeros( (n2, 1) )
            matrixx0 = np.zeros( (n2, 1) )
            for i in range(0,n2):
                for j in range(0,n2):
                    matrixa[i][j] = elementsa[(i*n2) + j]
                    
            for j in range(0,n2):
                matrixb[j][0] = elementsb[j]

            for j in range(0,n2):
                matrixx0[j][0] = elementsx0[j]

            matrixs,error,T,C,message = GaussSeidel.evaluate(matrixa,matrixb,matrixx0,Tol,Iter)

    return render(request, 'methods/equation_systems/gaussSeidel.html', {
            "size":request.session['matrix_size'],'T':T,'C':C, "form2":Matrix2(),"form": Matrix(),'matrix1':matrixa,'matrixb':matrixb,'matrixx0':matrixx0, "element": MatrixElement(),"error":error ,"message": message, "stages":stages, "matrixs": matrixs
    })

def jacobi_view(request, *args, **kwargs):
    message = ''
    stages = []
    matrixs = []
    matrixa=[]
    matrixb=[]
    error = []
    matrixx0=[]
    T=[]
    C=[]
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


            # variables
            
            n = request.session['matrix_size'] * request.session['matrix_size']
            n2= request.session['matrix_size']
            n3 = request.session['matrix_size'] * request.session['matrix_size'] +n2
            elementsa = elements[:n]
            elementsb = elements[n:]
            elementsx0 = elements[n3:]
            matrixa = np.zeros( (n2, n2) )
            matrixb = np.zeros( (n2, 1) )
            matrixx0 = np.zeros( (n2, 1) )
            for i in range(0,n2):
                for j in range(0,n2):
                    matrixa[i][j] = elementsa[(i*n2) + j]
                    
            for j in range(0,n2):
                matrixb[j][0] = elementsb[j]

            for j in range(0,n2):
                matrixx0[j][0] = elementsx0[j]

            matrixs,error,T,C,message = Jacobi.evaluate(matrixa,matrixb,matrixx0,Tol,Iter)

    return render(request, 'methods/equation_systems/jacobi.html', {
            "size":request.session['matrix_size'],'T':T,'C':C, "form2":Matrix2(),"form": Matrix(),'matrix1':matrixa,'matrixb':matrixb,'matrixx0':matrixx0, "element": MatrixElement(),"error":error ,"message": message, "stages":stages, "matrixs": matrixs
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







def pivot_view(request, *args, **kwargs):
    default = True
    a = [[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]]
    b = [1,1,1,1]
    if request.method == 'POST':
        method = request.POST['method']
        dim = int(request.POST['dim'])
        a = toMatrix(request.POST.getlist('a'), dim)
        b = request.POST.getlist('b')
        request.session['dim'] = dim
        request.session['a'] = a
        request.session['b'] = b

        steps =[]
        solution = []
        message = ''
        if method == 'Partial':
            steps, solution, message = partial_pivot.gauss(a,b)
        elif method == 'Total':
            steps, solution, message = total_pivot.gauss(a,b)
        
        solved = False
        if np.any(steps):
            if np.any(solution):
                solved = True

        return render(request, 'methods/equation_systems/pivot.html',
        {'steps': steps, 'solution': solution, 'aMatrix': request.session['a'], 'bMatrix': request.session['b'], 'dim': request.session['dim'], 'message': message, 'solved':solved})
    return render(request, 'methods/equation_systems/pivot.html', {'default': default, 'a': a, 'b':b})

def toMatrix(matrix, rows):
    m = []
    for i in range(0,len(matrix),rows):
        n = []
        for j in range(i,i+rows):
            n.append(matrix[j])
        m.append(n)
    return m