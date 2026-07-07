from django.shortcuts import render
from .forms import UserLoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            # authenticate() verifies that the user credentials are valid. It returns None if not valid
            user = authenticate(request, email=form_data['email'], password=form_data['password'])
            if user is not None:
                # verify the user is an active
                if user.is_active:
                    # login() saves the user’s ID in the session login() saves the user’s ID in the session through Django’s session framework
                    login(request, user)
                    return HttpResponseRedirect('/redirected-to-profile-dashboard')
                else: 
                    return HttpResponse('User account disabled')
            else:
                return HttpResponse('Login invalid. Please contact administrator.')
        
    else:
        form = UserLoginForm()
    
    return render(request, "users/login.html", {"form": form})

