from django.contrib import admin
from .models import Category, Author, Genre, Books, Reviews

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Books)
admin.site.register(Reviews)
