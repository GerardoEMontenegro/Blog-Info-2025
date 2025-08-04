from django.shortcuts import redirect, render
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, AvatarUpdateForm
from django.contrib.auth import login, logout
from .models import User



class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['posts'] = user.posts.all().order_by('-created_at')
        return context
    
class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = AvatarUpdateForm
    template_name = 'user/update_avatar.html'
    success_url = reverse_lazy('user:user_profile')  # Ajustá según el nombre real de tu URL de perfil

    def get_object(self):
        return self.request.user


from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm  # Asegúrate de importar tu formulario personalizado

class Registro_View(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'auth/auth_register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        registered_group = Group.objects.get(name='Registered')  # Asegúrate que el grupo exista
        self.object.groups.add(registered_group)  # Aquí se corrige el método
        return response
        

    def get_form(self, form_class=None):
        """
        Sobrescribimos get_form para pasar request.FILES al formulario (para avatar)
        """
        form_class = self.get_form_class()
        return form_class(self.request.POST or None, self.request.FILES or None)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user:user_profile')
        return super().dispatch(request, *args, **kwargs)


class Login_View(FormView):
    template_name = 'auth/auth_login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('user:user_profile')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user:user_profile')
        return super().dispatch(request, *args, **kwargs)
    
class Logout_View(RedirectView):
    template_name = 'auth/auth_login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('user:login')


# class LogoutView(TemplateView):
#     template_name = 'auth_logout.html'
    
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)