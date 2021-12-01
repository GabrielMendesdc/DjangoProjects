from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views


app_name = 'users'
template_name = 'users/login.html'

urlpatterns = [
    #pagina de login
    re_path(r'^login/$', LoginView.as_view(), name = 'login'),

    #pagina de logout
    re_path(r'^logout/$', views.logout_view, name="logout"),
    
    #pagina de cadastro
    re_path(r'^register/$', views.register, name='register'),
]