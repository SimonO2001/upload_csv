from django import template

register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    if hasattr(value, str(arg)):
        return getattr(value, arg)
    else:
        return "Attribute not found"
