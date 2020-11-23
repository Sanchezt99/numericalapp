from django import forms


class FixedPointForm(forms.Form):
    F = forms.CharField(label='Function f')
    G = forms.CharField(label='Function g')
    x0 = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')

class NewtonForm(forms.Form):
    F = forms.CharField(label='Function f')
    FPrime = forms.CharField(label='Function fprime')
    x0 = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')

class SecantForm(forms.Form):
    F = forms.CharField(label='Function f')
    x0 = forms.DecimalField(label='Initial x (x0)')
    x1 = forms.DecimalField(label='Initial x (x1)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')