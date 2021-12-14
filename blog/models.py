from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True)
    cover = models.ImageField(upload_to="media/categoryCover", blank=True, null=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICE = (
        ('p', 'publish'),
        ('d', 'draft'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True)
    content = models.TextField()
    cover = models.ImageField(upload_to="articleCover")
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category, related_name='articles')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)

    def __str__(self):
        return self.title
