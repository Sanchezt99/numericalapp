from pydoc import html
from django.shortcuts import render
from .Forms import vandermonde, newtondivdif
from .Methods import lineal_spline, cubic_spline, quadratic_spline, lagrange


# Create your views here.

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
    return render(request, 'methods/interpolation/vandermonde.html', {})





    

def newtondivdif_view(request, *args, **kwargs):
    return render(request, 'methods/interpolation/newtondivdif.html', {})





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

