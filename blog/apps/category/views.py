from django.views.generic import TemplateView

# Create your views here.from django.views.generic import TemplateView


class CategoryDetailView(TemplateView):
    template_name = 'category/category_detail.html'
