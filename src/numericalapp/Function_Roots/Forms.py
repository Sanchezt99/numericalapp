from django import forms


class MultipleRootsForm(forms.Form):
    F = forms.CharField(label='Function f')
    FP = forms.CharField(label="Function f' (First derivative of f) ")
    F2P = forms.CharField(label="Function f'' (Second derivative of f) ")
    x0 = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')


class FixedPointForm(forms.Form):
    F = forms.CharField(label='Function f')
    G = forms.CharField(label='Function g')
    x0 = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')

class NewtonForm(forms.Form):
    F = forms.CharField(label='Function f')
    FPrime = forms.CharField(label='Function fprime')
    xi = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')

class SecantForm(forms.Form):
    F = forms.CharField(label='Function f')
    x0 = forms.DecimalField(label='Initial x (x0)')
    x1 = forms.DecimalField(label='Initial x (x1)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')