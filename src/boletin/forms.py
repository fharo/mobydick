from django import forms

class RegForm(forms.Form):
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    edad = forms.IntegerField()
