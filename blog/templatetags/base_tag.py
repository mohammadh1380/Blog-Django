from django import template

register = template.Library()


@register.simple_tag
def title(t="Project"):
    return t
