from django import template
import re

register = template.Library()

@register.filter(name='razdvoji_rijeci_filter')
def razdvoji_rijeci(value):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', value)