from django.contrib import admin
from .models import Article, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'slug')
    prepopulated_fields = {"slug": ("title",)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish', 'slug')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
