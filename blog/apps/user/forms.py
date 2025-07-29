from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'user_name', 'email', 'avatar', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise forms.ValidationError("El nombre de usuario no puede contener espacios.")
        if len(username) < 4:
            raise forms.ValidationError("Debe tener al menos 4 caracteres.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Solo se permiten correos de Gmail.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if not any(char in "!@#$%^&*()" for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos un símbolo especial.")
        return password