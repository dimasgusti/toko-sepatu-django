from django import template

register = template.Library()

@register.filter
def rupiah_format(value):
    value = int(value)
    formatted_value = f"{value:,}"
    return f"Rp {formatted_value}"