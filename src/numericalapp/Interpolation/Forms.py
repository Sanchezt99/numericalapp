from django import forms

class splainForm(forms.Form):
    x = forms.DecimalField()
    y = forms.DecimalField()
    x.widget.attrs.update({'id' : 'x_input'})
    y.widget.attrs.update({'id' : 'y_input'})