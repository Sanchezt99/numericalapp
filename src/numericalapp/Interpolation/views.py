from pydoc import html
from django.shortcuts import render
from .Forms import splainForm, vandermonde, newtondivdif, lagrange, neville
import django.utils.html
from .Methods import lineal_spline, cuadratic_splain, cubic_spline


# Create your views here.

def splains_view(request, *args, **kwargs):
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
        elif method == 'Cuadratic':
            tracers, coefficients, message = cuadratic_splain.splain(x,y)
        else:
            tracers, coefficients, message = cubic_spline.splain(x,y)

        return render(request, 'methods/interpolation/splains.html',
        {'range': range(10), 'tracers': tracers, 'coefficients': coefficients, 'xSplain': request.session['x'], 'ySplain': request.session['y'], 'message': message})
    return render(request, 'methods/interpolation/splains.html', {'range': range(10), 'default': True})
def vandermonde_view(request, *args, **kwargs):
    form = splainForm()
    return render(request, 'methods/interpolation/vandermonde.html', {'form': form, 'range': range(10)})
def newtondivdif_view(request, *args, **kwargs):
    form = splainForm()
    return render(request, 'methods/interpolation/newtondivdif.html', {'form': form, 'range': range(10)})
def lagrange_view(request, *args, **kwargs):
    form = splainForm()
    return render(request, 'methods/interpolation/lagrange.html', {'form': form, 'range': range(10)})
def neville_view(request, *args, **kwargs):
    form = splainForm()
    return render(request, 'methods/interpolation/neville.html', {'form': form, 'range': range(10)})



