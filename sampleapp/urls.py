from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("article/<int:pk>", views.articles, name="articles"),
    path("contents/", views.contents, name="contents"),
    path("trending/", views.trending, name="trending"),
    path("exclusive_insight/", views.exclusive_insight, name="exclusive_insight"),
]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)