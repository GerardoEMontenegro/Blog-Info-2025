from django.urls import path
from apps.category import views as views

app_name = 'category'

urlpatterns = [
    path('category/<int/pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/lista', views.CategoryListView.as_view(), name='category_list'),
    path('category/crear', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/actualizar', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/eliminar', views.CategoryDeleteView.as_view(), name='category_delete'),
    
]
