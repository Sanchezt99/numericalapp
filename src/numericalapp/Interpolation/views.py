from django.shortcuts import render
from sympy.simplify.simplify import clear_coefficients
from .Forms import splainForm

from .Methods import lineal_spline

# Create your views here.

def splains_view(request, *args, **kwargs):
    if request.method == 'POST':
        x = request.POST.getlist('x')
        y = request.POST.getlist('y')

        tracers, coefficients = lineal_spline.splain(x,y)
        return render(request, 'methods/interpolation/splains.html', {'range': range(10), 'tracers': tracers, 'coefficients': coefficients})

    return render(request, 'methods/interpolation/splains.html', {'range': range(10)})