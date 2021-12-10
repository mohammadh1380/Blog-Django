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


# class authUsers(User):
#     def user(self):
#         if User.is_staff:
#             return User


class Article(models.Model):
    STATUS_CHOICE = (
        ('p', 'publish'),
        ('d', 'draft'),
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True)
    content = models.TextField()
    cover = models.ImageField(upload_to="media/articleCover")
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)

    def __str__(self):
        return self.title
