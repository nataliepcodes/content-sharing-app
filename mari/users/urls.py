from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', include('django.contrib.auth.urls'))
]