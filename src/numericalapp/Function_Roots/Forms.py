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
    xi = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')

class SecantForm(forms.Form):
    F = forms.CharField(label='Function f')
    x0 = forms.DecimalField(label='Initial x (x0)')
    x1 = forms.DecimalField(label='Initial x (x1)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')

class incrementalsearchForm(forms.Form):
    F = forms.CharField(label='Function f')
    x0 = forms.DecimalField(label='Initial value')
    Delta = forms.DecimalField(label='Delta')
    Iter = forms.IntegerField(label='Iterations')

class bisectionForm(forms.Form):
    F = forms.CharField(label='Function f')
    a = forms.DecimalField(label='Lower interval value (a)')
    b = forms.DecimalField(label='Higher interval value (b)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')

class falsepositionForm(forms.Form):
    F = forms.CharField(label='Function f')
    a = forms.DecimalField(label='Lower interval value (a)')
    b = forms.DecimalField(label='Higher interval value (b)')
    Tol = forms.DecimalField(label='Tolerance')
    Iter = forms.IntegerField(label='Iterations')