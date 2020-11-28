from pydoc import html
from django.shortcuts import render
from .Forms import vandermonde, newtondivdif
from .Methods import lineal_spline, cubic_spline, quadratic_spline, lagrange,Newton_Divided_Difference, lagrange, vandermonde
from django import forms

# Create your views here.
class Matrix(forms.Form):
    rows = forms.IntegerField(min_value=2, max_value=8,)

class MatrixElement(forms.Form):
    element = forms.FloatField(label=False, widget=forms.NumberInput(attrs={'size': '5'}),initial=1)

  
def splines_view(request, *args, **kwargs):
    if request.method == 'POST':
        method = request.POST['method']
        x = request.POST.getlist('x')
        y = request.POST.getlist('y')
        request.session['xInterpolation'] = x
        request.session['yInterpolation'] = y

        coefficients =[]
        tracers = []
        message = ''
        if method == 'Lineal':
            tracers, coefficients, message = lineal_spline.splain(x,y)
        elif method == 'Quadratic':
            tracers, coefficients, message = quadratic_spline.splain(x,y)
        else:
            tracers, coefficients, message = cubic_spline.splain(x,y)

        return render(request, 'methods/interpolation/splines.html',
        {'tracers': tracers, 'coefficients': coefficients, 'xInterpolation': request.session['xInterpolation'], 'yInterpolation': request.session['yInterpolation'], 'message': message})

    default = False if ('xInterpolation' in request.session and 'yInterpolation' in request.session) else True
    if default:
        return render(request, 'methods/interpolation/splines.html', {'default': default})
    return render(request, 'methods/interpolation/splines.html',
    {'default': default,'xInterpolation': request.session['xInterpolation'], 'yInterpolation': request.session['yInterpolation']})

def vandermonde_view(request, *args, **kwargs):
    if request.method == 'POST':
        x      = request.POST.getlist('x')
        y      = request.POST.getlist('y')
        request.session['xInterpolation'] = x
        request.session['yInterpolation'] = y

        A           = []
        vPolynomial = []
        message     = ''
        A, vPolynomial, message = vandermonde.Vandermonde(x,y)
        print(A,vPolynomial)
        return render(request, 'methods/interpolation/vandermonde.html',
        {'aMatrix': A, 'vPolynomial': vPolynomial, 'xInterpolation': request.session['xInterpolation'], 'yInterpolation': request.session['yInterpolation'], 'message': message})

    default = False if ('xInterpolation' in request.session and 'yInterpolation' in request.session) else True

    if default:
        return render(request, 'methods/interpolation/vandermonde.html', {'default': default})
    return render(request, 'methods/interpolation/vandermonde.html',
    {'default': default,'xInterpolation': request.session['xInterpolation'], 'yInterpolation': request.session['yInterpolation']})





    

def newtondivdif_view(request, *args, **kwargs):
    term     = []
    salida      = []
    polinomio = ''
    polisimple = ''
    x= []
    y = []
    message = ""
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
            x = elements[:request.session['matrix_size']]
            y = elements[request.session['matrix_size']:]
            print(x)
            print(y)
            term,salida, polinomio,polisimple, message= Newton_Divided_Difference.evaluate(x,y)
       
        


    return render(request, 'methods/interpolation/newtondivdif.html',
        {"element": MatrixElement(),"size":request.session['matrix_size'], "form": Matrix(),'term': term, 'salida': salida, 'message': message, 'polinomio' : polinomio , 'polisimple':polisimple, 'x':x, 'y':y})






def lagrange_view(request, *args, **kwargs):
    if request.method == 'POST':
        x      = request.POST.getlist('x')
        y      = request.POST.getlist('y')
        request.session['xInterpolation'] = x
        request.session['yInterpolation'] = y

        lps     = []
        lp      = []
        message = ''
        lps, lp, message = lagrange.lagrange(x,y)

        return render(request, 'methods/interpolation/lagrange.html',
        {'lps': lps, 'lp': lp, 'xInterpolation': request.session['xInterpolation'], 'yInterpolation': request.session['yInterpolation'], 'message': message})

    default = False if ('xInterpolation' in request.session and 'yInterpolation' in request.session) else True

    if default:
        return render(request, 'methods/interpolation/lagrange.html', {'default': default})
    return render(request, 'methods/interpolation/lagrange.html',
    {'default': default,'xInterpolation': request.session['xInterpolation'], 'yInterpolation': request.session['yInterpolation']})

