from django.urls import path
from . import views

app_name = 'users'

url_patters = [
    path('/login', views.login_view, name='login'),
]