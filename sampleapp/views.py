from django.shortcuts import render

from . import models


def index(request):
    context_data = {
        "articles": models.Article.objects.order_by('-published_at')[:2],
        "editor_section": models.Article.objects.order_by('published_at')[:6],
        "columns": models.Article.objects.order_by('?')[:3],
    }
    print(context_data)
    return render(request, "index.html", context_data)


def articles(request, pk):
    context_data = {
        "article": models.Article.objects.filter(id=pk).first(),
    }
    return render(request, "articles.html", context_data)


def contents(request):
    context_data = {
        "articles": models.Article.objects.all(),
    }
    return render(request, "contents.html", context_data)


def main_slidebar(request):
    context_data = {
        "Mainslidebarcd sa": models.Main_slidebar.objects.first()
    }
    return render(request, "Main_slidebar.html", context_data)


def trending(request):
    context_data = {

        "articles": models.Article.objects.all(),
    }
    return render(request, "trending.html", context_data)


def exclusive_insight(request):
    context_data = {

    }
    return render(request, "exclusive_insight.html", context_data)
