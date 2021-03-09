from django.urls import include, path, re_path
from myapp.views import index, main_article, main_articles_archive, \
    article, user, users, correct_number, specific
from django.contrib import admin

urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('articles/', main_article, name='mail_article'),
    path('articles/archive/', main_articles_archive, name='main_articles_archive'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:name>', article, name='article_name'),
    path('users/', user, name='users'),
    path('users/<int:user_id>/', users, name='user'),
    re_path(r'^(?P<phone_number>^050\d{7}|099\d{7})/$', correct_number, name='correct_number'),
    re_path(r'^(?P<line>^[a-f0-9]{4}\-[a-f0-9]{6})/$', specific, name='specific'),
]