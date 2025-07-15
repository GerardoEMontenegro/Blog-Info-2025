from django.forms import ModelForm
from .models import post

 
class postform(ModelForm):
    class Meta:
        model = post
        fields = ['titulo', 'contenido']
        
