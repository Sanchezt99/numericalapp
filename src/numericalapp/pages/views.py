from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request,*args,**kwargs):
    return render(request,'index.html',{})

def methods_view(request,*args,**kwargs):
    return render(request,'methods.html',{})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html',{})
    
def help_view(request, *args, **kwargs):
    return render(request, 'help.html',{})

