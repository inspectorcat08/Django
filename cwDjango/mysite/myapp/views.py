from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    return HttpResponse("Hey! It's your first view!!")


def index(request):
    return HttpResponse("It's index page!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def archive(request):
    return HttpResponse('This is archive')


def users(request, user_number):
    return HttpResponse("This is an article #{}.".format(user_number))


def article(request, article_number, slug_text=''):
    return HttpResponse("This is an article #{}. {}".format(article_number, "Name of this article is {}".format(slug_text) if slug_text else "This is unnamed article"))


def archive_number(request, article_number, name=''):
    return HttpResponse(("This is an archive number #{}. {}".format(article_number, "Name of this article is {}".format(name) if name else "This is unnamed article")))


def phone_number(request, number):
    return HttpResponse(f'The phone number +38{number} was validated')


def new_url(request, line):
    return HttpResponse(f'New url {line} was validated')