from django import forms

class splainForm(forms.Form):
    x = forms.DecimalField()
    y = forms.DecimalField()
    x.widget.attrs.update({'id' : 'x_input'})
    y.widget.attrs.update({'id' : 'y_input'})

class vandermonde(forms.Form):
    x = forms.DecimalField()
    y = forms.DecimalField()
    x.widget.attrs.update({'id' : 'x_input'})
    y.widget.attrs.update({'id' : 'y_input'})

class newtondivdif(forms.Form):
    x = forms.DecimalField()
    y = forms.DecimalField()
    x.widget.attrs.update({'id' : 'x_input'})
    y.widget.attrs.update({'id' : 'y_input'})

class lagrange(forms.Form):
    x = forms.DecimalField()
    y = forms.DecimalField()
    x.widget.attrs.update({'id' : 'x_input'})
    y.widget.attrs.update({'id' : 'y_input'})

class neville(forms.Form):
    x = forms.DecimalField()
    y = forms.DecimalField()
    x.widget.attrs.update({'id' : 'x_input'})
    y.widget.attrs.update({'id' : 'y_input'})