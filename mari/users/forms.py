from django import forms

class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.Charfield(widget=forms.PasswordInput)