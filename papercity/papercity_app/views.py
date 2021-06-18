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
        try:
            query = self.request.GET.get('q')
            a = "".join(query[0].upper()) + query[1:]
            object_list = Books.objects.filter(Q(title__icontains=a) | Q(author__name__icontains=a))
            return object_list
        except IndexError:
            pass

class BookView(ListView):
    """Список книг"""

    model = Books
    template_name = "papercity_app/book_list.html"
    context_object_name = "book_list"

    def get_queryset(self):
        return Books.objects.order_by('-id')

    def category_list(request, url):
        books = Books.objects.filter(category__url=url)
        category_menu = Category.objects.all()
        return render(request, "papercity_app/book_list.html", {"book_list": books, "category_menu": category_menu})


class BookDetailView(DetailView):
    """Страница с книгой"""

    model = Books
    template_name = "papercity_app/book_detail.html"
    slug_field = "url"
    context_object_name = "book"


class CategoryList(ListView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = "categories"
    template_name = "papercity_app/book_list.html"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Books.objects.get(id=pk)
        if form.is_valid:
            form = form.save(commit=False)
            form.book_id = pk
            form.save()
        return redirect(book.get_absolute_url())

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
