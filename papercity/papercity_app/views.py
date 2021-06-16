from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Books, Category
from .forms import ReviewForm
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


class Search(ListView):
    model = Books
    template_name = 'papercity_app/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        a = "".join(query[0].upper()) + query[1:]
        object_list = Books.objects.filter(Q(title__icontains=a) | Q(author__name__icontains=a))
        return object_list


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

def home(request):
    return render(request, 'papercity_app/home.html')


def selection1(request):
    return render(request, 'papercity_app/selection1.html')


def selection2(request):
    return render(request, 'papercity_app/selection2.html')


def selection3(request):
    return render(request, 'papercity_app/selection3.html')


def selection4(request):
    return render(request, 'papercity_app/selection4.html')


def stocks(request):
    return render(request, 'papercity_app/stocks.html')


def selection_all(request):
    return render(request, 'papercity_app/selection_all.html')
