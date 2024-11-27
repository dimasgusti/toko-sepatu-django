from django import template

register = template.Library()

@register.filter
def rupiah_format(value):
    # Ensure the value is an integer (remove decimals)
    value = int(value)
    # Format the number with commas as thousand separators and ensure 'Rp' is capitalized
    formatted_value = f"{value:,}"
    return f"Rp {formatted_value}"