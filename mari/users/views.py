from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            """
            authenticate() verifies that the user credentials are valid. It returns None if not valid
            authenticate() checks is_active and rejects users with is_active=False in Django version 6.0.x 
            Thus, authenticate() will return False for the user accounts that are disabled
            More in https://github.com/django/django/tree/stable/6.0.x/django
            Search for 'def user_can_authenticate function' in django.contrib.auth.backends in class ModelBackend
            """
            user = authenticate(request, username=form_data['email'], password=form_data['password'])
            if user is not None:
                # login() saves the user’s ID in the session login() saves the user’s ID in the session through Django’s session framework
                login(request, user)
                return HttpResponseRedirect('/redirected-to-profile-dashboard')
            else:
                return HttpResponse('Login invalid. Please contact administrator.')
        
    else:
        form = UserLoginForm()
    
    return render(request, "registration/login.html", {"form": form})

@login_required
def dashboard_view(request):
    return render(request, 'user/dashboard.html', {'section': 'dashboard'})
