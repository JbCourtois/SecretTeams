from django import forms


class GenerateForm(forms.Form):
    seed = forms.CharField(max_length=20)
    teams = forms.CharField()
