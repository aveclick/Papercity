from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Books, Category, Cart
from .forms import ReviewForm
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse


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

def add_to_cart(request):
    context = {}
    items = Cart.objects.filter(user__id=request.user.id, status=False)
    context["items"] = items

    if request.user.is_authenticated:
        if request.method == "POST":
            pid = request.POST["pid"]
            qty = request.POST["qty"]
            is_exist = Cart.objects.filter(book__id=pid, user__id=request.user.id, status=False)
            if len(is_exist) > 0:
                context["msz"] = "Товар уже добавлен в Вашу корзину"
                context["cls"] = "alert alert-warning"
            else:
                book = get_object_or_404(Books, id=pid)
                usr = get_object_or_404(User, id=request.user.id)
                c = Cart(user=usr, book=book, count=qty)
                c.save()
                context["msz"] = "{} добавлен в Вашу корзину".format(book.title)
                context["cls"] = "alert alert-success"
    else:
        context["status"] = 'Для добавления товара в корзину необходимо войти в аккаунт.'
    return render(request, "papercity_app/cart.html", context)

def get_cart_data(request):
    items = Cart.objects.filter(user__id=request.user.id, status=False)
    total, count = 0, 0
    for item in items:
        total += float(item.book.price) * item.count
        count += int(item.count)

    res = {
        "total": total, "quan": count,
    }
    return JsonResponse(res)


def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(Cart, id=cid)
        cart_obj.count = qty
        cart_obj.save()
        return HttpResponse(cart_obj.count)

    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(Cart, id=id)
        cart_obj.delete()
        return HttpResponse(1)

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
