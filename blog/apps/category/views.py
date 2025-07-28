from django.views.generic import TemplateView

# Create your views here.from django.views.generic import TemplateView


class CategoryDetailView(TemplateView):
    template_name = 'category/category_detail.html'

class CategoryListView(TemplateView):
    template_name = 'category/category_list.html'

class CategoryCreateView(TemplateView):
    template_name = 'category/category_create.html'

class CategoryUpdateView(TemplateView):
    template_name = 'category/category_update.html'

class CategoryDeleteView(TemplateView):
    template_name = 'category/category_delete.html'

    
