from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Article, Category


# Create your views here.

class HomeView(generic.ListView):
    queryset = Article.objects.filter(status='p')
    template_name = 'blog/home.html'
    context_object_name = 'articles'
    ordering = ['-publish']
    paginate_by = 2


class PostView(generic.DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.filter(status='p'), slug=slug)

    template_name = 'blog/post.html'
    context_object_name = 'article'


class CategoriesList(generic.ListView):
    template_name = 'blog/Categories.html'
    queryset = Category.objects.filter(status=True)
    context_object_name = 'categories'


class CategoryView(generic.DetailView):
    template_name = 'blog/Category_detail.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Category.objects.filter(status=True), slug=slug)

    context_object_name = 'category'


class CreateArticle(generic.CreateView):
    template_name = "blog/create_article.html"


class DeleteArticle(generic.DetailView):
    template_name = "blog/delete_article.html"


class UpdateArticle(generic.UpdateView):
    template_name = "blog/update_article.html"


class Contact(generic.TemplateView):
    template_name = "blog/contact.html"
