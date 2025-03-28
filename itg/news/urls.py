from django.urls import path

from news.views import contacts, get_all_news, get_news_by_id, main

urlpatterns = [
    path("", main, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("news/", get_all_news, name="archive"),
    path("<int:news_id>/", get_news_by_id, name="news_detail"),
]
