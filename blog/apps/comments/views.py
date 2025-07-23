from django.views.generic import TemplateView

# Create your views here.from django.views.generic import TemplateView


#class CommentsDetailView(TemplateView):
 #   template_name = '.html'

#class CommentsListView(TemplateView):
  #  template_name = '..._list.html'

class CommentsCreateView(TemplateView):
    template_name = 'comments/comments_create.html'

class CommentsUpdateView(TemplateView):
    template_name = 'comments/comments_update.html'

class CommentsDeleteView(TemplateView):
    template_name = 'comments/comments_delete.html'

    
