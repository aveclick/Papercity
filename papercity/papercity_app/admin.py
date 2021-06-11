from django.contrib import admin
from .models import Category, Author, Subcategory, Books, Reviews

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")
    list_filter = ("author", "category")
    search_fields = ("title", "author__name", "category__name")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url")

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "book", "id")
    readonly_fields = ("name",)


admin.site.register(Author)
admin.site.register(Subcategory)
