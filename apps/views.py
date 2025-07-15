from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import postform 
from .models import post

def home(request):
    return render(request, 'home.html')


def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm})
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('mis_posts')
            except IntegrityError:
                return render(request, 'registro.html', 
                              {'form': UserCreationForm, 
                               'error': "El usuario ya existe."})
        else:
            return render(request, 'registro.html', 
                          {'form': UserCreationForm, 
                           'error': "Las contraseñas no coinciden."})





def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
        if request.method == 'GET':
             return render(request, 'signin.html', 
                      {'form': AuthenticationForm})

        else:
            user = authenticate(request, username=request.POST['username'], 
            password=request.POST['password'])
            if user is None:
                 return render(request, 'signin.html', 
                      {'form': AuthenticationForm, 
                       'error': "Usuario o contraseña incorrectos."})
            else:
                login(request, user)
                return redirect('home')
                 

def crear_post(request):
    if request.method == 'GET':
         return render(request, 'crear_post.html', {'form': postform})
    else:
        try:
            form = postform(request.POST)
            new_post = form.save(commit=False)
            new_post.usuario = request.user
            new_post.save()
            return redirect('mis_posts')
        except ValueError:
            return render(request, 'crear_post.html', 
                          {'form': postform, 
                           'error': "Por favor, corrija los errores."})
        

def mis_posts(request):
        mis_posts = post.objects.filter(usuario=request.user)
        return render(request, 'mis_posts.html', {'mis_posts': mis_posts})

def detalle_post(request, post_id):
     en_post = get_object_or_404(post, id=post_id)
     return render(request, 'detalle_post.html', {'post': en_post})
