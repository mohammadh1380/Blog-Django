# Generated by Django 4.0 on 2021-12-11 19:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='media/categoryCover')),
                ('status', models.BooleanField(default=True)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('content', models.TextField()),
                ('cover', models.ImageField(upload_to='media/articleCover')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('p', 'publish'), ('d', 'draft')], max_length=1)),
                ('category', models.ManyToManyField(to='blog.Category')),
            ],
        ),
    ]
