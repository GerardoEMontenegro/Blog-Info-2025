from django.urls import path
from apps.user.views import Registro_View, Login_View, UserProfileView, Logout_View
# from django.contrib.auth.views import LogoutView

app_name = 'user'

# class MyLogoutView(LogoutView):
#     http_method_names = ['get', 'post']  # Permitimos GET y POST

urlpatterns = [
    path('user/profile', UserProfileView.as_view(), name='user_profile'),
    path('login/', Login_View.as_view(), name='login'),
    path('registro/', Registro_View.as_view(), name='registro'),
    path('logout/', Logout_View.as_view(), name='logout'),
]