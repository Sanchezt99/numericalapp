from pydoc import html
from django.shortcuts import render
from .Forms import splainForm, vandermonde, newtondivdif, lagrange, neville
from .Methods import lineal_spline, cubic_spline, quadratic_spline


# Create your views here.

def splines_view(request, *args, **kwargs):
    if request.method == 'POST':
        method = request.POST['method']
        x = request.POST.getlist('x')
        y = request.POST.getlist('y')
        request.session['x'] = x
        request.session['y'] = y

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
        {'tracers': tracers, 'coefficients': coefficients, 'xSplain': request.session['x'], 'ySplain': request.session['y'], 'message': message})
    return render(request, 'methods/interpolation/splines.html', {'default': True})

def vandermonde_view(request, *args, **kwargs):
    return render(request, 'methods/interpolation/vandermonde.html', {})





    

def newtondivdif_view(request, *args, **kwargs):
    return render(request, 'methods/interpolation/newtondivdif.html', {})





def lagrange_view(request, *args, **kwargs):
    return render(request, 'methods/interpolation/lagrange.html', {})

