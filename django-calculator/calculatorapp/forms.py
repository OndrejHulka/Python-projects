from django import forms

class NumbersForms(forms.Form):
    first_number = forms.FloatField()
    second_number = forms.FloatField()