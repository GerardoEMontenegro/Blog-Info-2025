from django.views.generic import TemplateView
from apps.post.models import Post





class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener los últimos 5 posts publicados
        context['ultimos_posts'] = Post.objects.filter(
            
        ).order_by('-created_at')[:5]
        return context



