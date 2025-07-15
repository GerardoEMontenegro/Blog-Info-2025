from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def registro(request):
    if request.method == 'GET':
        return render(request, 'registracion.html', {'form': UserCreationForm()})
