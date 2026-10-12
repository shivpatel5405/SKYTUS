from django import template

register = template.Library()

# Assessment 4 :- Question 4 — Custom Template Filters

@register.filter(name='truncate_words')
def truncate_words(value, num_words=5):
    """
    Truncates a string after a given number of words and appends '...'.
    Usage in template: {{ value|truncate_words:3 }}
    """
    if not isinstance(value, str):
        value = str(value)

    words = value.split()
    try:
        limit = int(num_words)
    except (ValueError, TypeError):
        limit = 5

    if len(words) > limit:
        return " ".join(words[:limit]) + "..."
    return value


@register.filter(name='highlight_author')
def highlight_author(value):
    """
    Prepends a pen icon and formats the author name.
    Usage in template: {{ book.author|highlight_author }}
    """
    return f"✍️ {value}"
