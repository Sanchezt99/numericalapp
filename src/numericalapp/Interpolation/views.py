from django.shortcuts import render
from .Forms import splainForm, vandermonde, newtondivdif, lagrange, neville

# Create your views here.

def splains_view(request, *args, **kwargs):
    form = splainForm()
    return render(request, 'methods/interpolation/splains.html', {'form': form, 'range': range(10)})
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