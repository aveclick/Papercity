from django import template
from papercity_app.models import Books

register = template.Library()

@register.inclusion_tag("papercity_app/tags/first_book.html")
def get_first_books():
    books = Books.objects.order_by("id")[:5]
    return {"first_books": books}

@register.inclusion_tag("papercity_app/tags/second_book.html")
def get_second_books():
    books = Books.objects.order_by("-id")[:5]
    return {"second_books": books}
