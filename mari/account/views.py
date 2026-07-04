from django.shortcuts import render
from django.http import HttpResponse
from . forms import LoginForm
from django.contrib.auth import authenticate, login

""" 
Authentification system sources: 
1) https://docs.djangoproject.com/en/6.0/topics/auth/default/
2) Django3 by Example, Antonio Mele, Third Edition, 2020
"""

def handle_login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            


