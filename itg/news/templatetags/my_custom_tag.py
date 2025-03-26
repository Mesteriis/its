from django import template

register = template.Library()

@register.simple_tag
def my_custom_tag(value):
    """
    Пример пользовательского тега, который просто возвращает переданное значение.
    """
    return value.upper()