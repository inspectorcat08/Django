from django.urls import include, path, re_path
from myapp.views import index, main_article, archive, users, article, archive_number, phone_number, new_url

urlpatterns = [
    path('my_url/', include('myapp.urls')),
    path('', index, name='index'),
    path('articles/', main_article, name='main_article'),
    path('articles/archive/', archive, name='archive'),
    path('users/', users, name='users'),
    path('articles/<int:article_number>', article, name='article'),
    path('articles/<int:article_number>/archive', archive_number, name='archive_number'),
    path('articles/<int:article_number>/<slug:slug_text>', article, name='archive'),
    path('users/<int:user_number>', users, name='user_number'),
    re_path(r'^(?P<number>^050\d{7}|099\d{7})/$', phone_number, name='correct_number'),
    re_path(r'^(?P<line>^[a-f0-9]{4}\-[a-f0-9]{6})/$', new_url, name='new_url'),
]