from django import forms


class MultipleRootsForm(forms.Form):
    F = forms.CharField(label='Function f')
    FP = forms.CharField(label="Function f' (First derivative of f) ")
    F2P = forms.CharField(label="Function f'' (Second derivative of f) ")
    x0 = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance',min_value=0.00000000000000001)
    Iter = forms.IntegerField(label='Iterations', min_value=1)


class FixedPointForm(forms.Form):
    F = forms.CharField(label='Function f')
    G = forms.CharField(label='Function g')
    x0 = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance',min_value=0.00000000000000001)
    Iter = forms.IntegerField(label='Iterations', min_value=1)

class NewtonForm(forms.Form):
    F = forms.CharField(label='Function f')
    FPrime = forms.CharField(label='Function fprime')
    xi = forms.DecimalField(label='Initial x (x0)')
    Tol = forms.DecimalField(label='Tolerance',min_value=0.00000000000000001)
    Iter = forms.IntegerField(label='Iterations', min_value=1)

class SecantForm(forms.Form):
    F = forms.CharField(label='Function f')
    x0 = forms.DecimalField(label='Initial x (x0)')
    x1 = forms.DecimalField(label='Initial x (x1)')
    Tol = forms.DecimalField(label='Tolerance',min_value=0.00000000000000001)
    Iter = forms.IntegerField(label='Iterations', min_value=1)

class incrementalsearchForm(forms.Form):
    F = forms.CharField(label='Function f')
    x0 = forms.DecimalField(label='Initial value')
    Delta = forms.DecimalField(label='Delta')
    Iter = forms.IntegerField(label='Iterations', min_value=1)

class bisectionForm(forms.Form):
    F = forms.CharField(label='Function f')
    a = forms.DecimalField(label='Lower interval value (a)')
    b = forms.DecimalField(label='Higher interval value (b)')
    Tol = forms.DecimalField(label='Tolerance',min_value=0.00000000000000001)
    Iter = forms.IntegerField(label='Iterations', min_value=1)

class falsepositionForm(forms.Form):
    F = forms.CharField(label='Function f')
    a = forms.DecimalField(label='Lower interval value (a)')
    b = forms.DecimalField(label='Higher interval value (b)')
    Tol = forms.DecimalField(label='Tolerance',min_value=0.00000000000000001)
    Iter = forms.IntegerField(label='Iterations', min_value=1)