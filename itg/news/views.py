from django.http import HttpResponse
from django.shortcuts import render

info = {
    'news_count': 100600,
    'users_count': 1000,
    'menu': ['Главная', 'О проекте', 'Каталог'],
}


def get_all_news(request):
    return render(request, 'news/catalog.html', info)


def get_news_by_id(request, news_id):
    return HttpResponse(f'Новость {news_id}')


def main(request):
    return render(request, 'main.html', info)
