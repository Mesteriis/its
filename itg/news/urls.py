from django.urls import path
from news.views import get_news_by_id, get_all_news, main
urlpatterns = [
    path('', main, name='index'),
    path('news/', get_all_news, name='news_list'),
    path('<int:news_id>/', get_news_by_id, name='news_info'),
]
