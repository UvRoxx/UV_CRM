from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def reduce_url(current_url):
    if len(current_url) > 20:
        return current_url[:20] + "..."
    else:
        return current_url
