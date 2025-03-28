from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from news.models import Article


def main(request):
    context = {
        "news_list": Article.objects.all()[:5],
    }
    return render(request, "catalog.html", context)


def contacts(request):
    return render(request, "contacts.html")


def get_all_news(request):
    context = {"news_list": Article.objects.all()}
    return render(request, "catalog.html", context)


def get_news_by_id(request, news_id):
    content = {"news": get_object_or_404(Article, pk=news_id)}
    return render(request, "news_detail.html", content)
