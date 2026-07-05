from django.urls import path
from . import views


url_patters = [
    path('/login', views.login_user, name='login'),
]