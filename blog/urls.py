from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, PostView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug:slug>/', PostView.as_view(), name='post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)