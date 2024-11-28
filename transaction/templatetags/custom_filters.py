# transaction/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='multiply_and_format')
def multiply_and_format(value, quantity):
    try:
        result = value * quantity
        return f"{result:.2f}"  # Format as float with two decimal places
    except (TypeError, ValueError):
        return value  # In case of invalid input, return the original value