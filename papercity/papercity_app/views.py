from django.shortcuts import render, redirect
from .models import Books, Category
from .forms import ReviewForm
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


class BookView(ListView):
    """Список книг"""

    def get(self, request):
        books = Books.objects.all().order_by('-id')
        category_menu = Category.objects.all()
        return render(request, "papercity_app/book_list.html", {"book_list": books, "category_menu": category_menu})

    def category_list(request, url):
        books = Books.objects.filter(category__url=url)
        category_menu = Category.objects.all()
        return render(request, "papercity_app/book_list.html", {"book_list": books, "category_menu": category_menu})


class BookDetailView(DetailView):
    """Страница с книгой"""

    def get(self, request, slug):
        book = Books.objects.get(url=slug)
        return render(request, "papercity_app/book_detail.html", {"book": book})


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.book_id = pk
            form.save()
        return redirect("/")
