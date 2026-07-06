from django.shortcuts import render
from .forms import UserLoginForm
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data
            # ...

            return HttpResponseRedirect("/redirected-to-profile-dashboard")
        
    else:
        form = UserLoginForm()
    
    return render(request, "users/login.html", {"form": form})

