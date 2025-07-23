from django.urls import path
from apps.comments import views as views

app_name = 'comments'

urlpatterns = [
    
    path('comments/crear', views.CategoryCreateView.as_view(), name='comments_create'),
    path('comments/actualizar', views.CategoryUpdateView.as_view(), name='comments_update'),
    path('comments/eliminar', views.CategoryDeleteView.as_view(), name='comments_delete'),
     
]
