from django.views.generic import TemplateView
from .models import Post
from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.utils.timezone import now
from django.contrib import messages
from django.shortcuts import redirect


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object  # <- Esto permite usar {{ post }} en el template
        return context
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        titulo = form.cleaned_data['title']
        contenido = form.cleaned_data['content']

        palabras_prohibidas = ['spam', 'prohibido', 'baneo']
        if any(p in titulo.lower() for p in palabras_prohibidas):
            form.add_error('title', 'El título contiene palabras no permitidas.')
            return self.form_invalid(form)

        if len(contenido) < 100:
            form.add_error('content', 'El contenido debe tener al menos 100 caracteres.')
            return self.form_invalid(form)

        hoy = now().date()
        posts_hoy = Post.objects.filter(author=user, created_at__date=hoy).count()
        if posts_hoy >= 3:
            form.add_error(None, "Ya has publicado el máximo de 3 posts hoy.")
            return self.form_invalid(form)

        form.instance.author = user
        return super().form_valid(form)




class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'post/post_update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_success_url(self):
        return reverse_lazy('user:user_profile')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('user:profile')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user



