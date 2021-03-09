from django import template
from random import randint, choice
from string import ascii_letters


register = template.Library()


@register.simple_tag
def random_number():
    return randint(1, 1000000)


@register.simple_tag
def random_name():
    return ''.join(choice(ascii_letters) for i in range(randint(5, 10)))

