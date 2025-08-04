from django.urls import path
from django.contrib.auth import views as auth_views
from apps.user.views import *
# from django.contrib.auth.views import LogoutView

app_name = 'user'

# class MyLogoutView(LogoutView):
#     http_method_names = ['get', 'post']  # Permitimos GET y POST

urlpatterns = [
    path('user/profile', UserProfileView.as_view(), name='user_profile'),
    path('login/', Login_View.as_view(), name='login'),
    path('registro/', Registro_View.as_view(), name='registro'),
    path('logout/', Logout_View.as_view(), name='logout'),
    path('user/update-avatar/', AvatarUpdateView.as_view(), name='update_avatar'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),

]