from django.shortcuts import render
from .Forms import splainForm

# Create your views here.

def splains_view(request, *args, **kwargs):
    form = splainForm()
    return render(request, 'methods/interpolation/splains.html', {'form': form, 'range': range(10)})