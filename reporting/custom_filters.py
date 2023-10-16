from django import template

register = template.Library()

@register.tag
def get_item(dictionary, key):
    return dictionary.get(key, '')

