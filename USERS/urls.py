from django.urls import path, re_path
from django.contrib.auth import login
from . import views

app_name = 'users'

urlpatterns = [
    #pagina de login
    re_path(r'^login/$', login, {'template_name': 'users/login.html'},
            name='login'),
]