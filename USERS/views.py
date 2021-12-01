from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    '''faz o logout'''
    logout(request)
    return HttpResponseRedirect(reverse('dozeros:index'))
    
def register(request):
    '''faz o cadastro de um novo usuário'''
    if request.method != 'POST':
        #exibe formulario branco
        form = UserCreationForm()
    else:
        #Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #faz login e redireciona
            authenticated_user = \
            authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('dozeros:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
