from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'allow_comments']
        labels = {
            'title': 'Título',
            'category': 'Categoría',
            'content': 'Contenido',
            'allow_comments': 'Permitir comentarios',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-textarea'}),
            'allow_comments': forms.CheckboxInput(),
        }