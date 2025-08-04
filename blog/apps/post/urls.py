from django.urls import path
from apps.post import views as views


app_name = 'post'

urlpatterns = [
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/editar/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<slug:slug>/borrar/', views.PostDeleteView.as_view(), name='post_delete'),
]