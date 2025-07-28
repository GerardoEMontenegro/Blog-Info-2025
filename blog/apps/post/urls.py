from django.urls import path
from apps.post import views as views

app_name = 'post'

urlpatterns = [
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/list', views.PostListView.as_view(), name='post_list'),
    path('posts/create', views.PostCreateView.as_view(), name='post_create'),
    path('posts/update', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/delete', views.PostDeleteView.as_view(), name='post_delete'),
     
]
