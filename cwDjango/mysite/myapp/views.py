from django.shortcuts import render, HttpResponse


def main_article(request):
    return render(request, 'main_article.html')


def main_articles_archive(request):
    return render(request, 'main_articles_archive.html')


def user(request):
    return render(request, 'user.html')


def article(request, article_id, name=''):
    return render(request, 'article_number.html', {
        'article_id': article_id,
        'slug_name': name,
    })


# def article(request, article_id, name=''):
#     if name:
#         if name == "archive":
#             return HttpResponse(f"This is an archive for #{article_id} article")
#         else:
#             return HttpResponse(f"This is an article #{article_id} with name - {name}")
#     else:
#         return HttpResponse(f"This is unnamed #{article_id} article")


def users(request, user_id):
    return HttpResponse(f'This is uniq answer for user {user_id}')


def correct_number(request, phone_number):
    return HttpResponse(f'The phone number +38{phone_number} was validated')


def specific(request, line):
    return HttpResponse(f'Specific code {line} was validated')


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')

    # контекст - словарь - передали данные в html
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
    })


def first(request):
    return render(request, 'first.html')


def base(request):
    return render(request, 'base.html')