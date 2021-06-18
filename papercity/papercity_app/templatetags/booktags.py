from django import template
from papercity_app.models import Books, Category

register = template.Library()

@register.inclusion_tag("papercity_app/tags/first_book.html")
def get_first_books():
    books = Books.objects.order_by("id")[:5]
    return {"first_books": books}

@register.inclusion_tag("papercity_app/tags/second_book.html")
def get_second_books():
    books = Books.objects.order_by("-id")[:5]
    return {"second_books": books}

@register.inclusion_tag("papercity_app/tags/empty_book.html")
def get_empty_books():
    books = Books.objects.order_by("-id")[:4]
    return {"empty_books": books}

@register.inclusion_tag("papercity_app/tags/new_books.html")
def get_new_books():
    books = Books.objects.order_by("-id")[:5]
    return {"new_books": books}

@register.inclusion_tag("papercity_app/tags/categories.html")
def get_categories():
    category = Category.objects.all()
    return {"categories": category}

