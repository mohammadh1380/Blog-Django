from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Article


# Create your views here.

class HomeView(generic.ListView):
    queryset = Article.objects.filter(status='p')
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    ordering = ['-publish']
    paginate_by = 2


class PostView(generic.DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.filter(status='p'), slug=slug)

    template_name = 'blog/post.html'
    context_object_name = 'article'
