from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.base import View
from .models import Books
from .forms import ReviewForm


def books(request):
    return render(request, 'papercity_app/books.html')

class BookDetailView(DetailView):
    def get(self, request, slug):
        book = Books.objects.get(url=slug)
        return render(request, "papercity_app/book.html", {"book": book})

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
            form.book_id = pk
            form.save()
        return redirect("/")

def cat1(request):
    return render(request, 'papercity_app/cat1.html')


def cat2(request):
    return render(request, 'papercity_app/cat2.html')


def cat3(request):
    return render(request, 'papercity_app/cat3.html')


def cat4(request):
    return render(request, 'papercity_app/cat4.html')


def cat5(request):
    return render(request, 'papercity_app/cat5.html')


def cat6(request):
    return render(request, 'papercity_app/cat6.html')


def cat7(request):
    return render(request, 'papercity_app/cat7.html')


def cat8(request):
    return render(request, 'papercity_app/cat8.html')


def cat9(request):
    return render(request, 'papercity_app/cat9.html')


def minicat1(request):
    return render(request, 'papercity_app/minicat1.html')


def minicat2(request):
    return render(request, 'papercity_app/minicat2.html')


def minicat3(request):
    return render(request, 'papercity_app/minicat3.html')


def minicat4(request):
    return render(request, 'papercity_app/minicat4.html')


def minicat5(request):
    return render(request, 'papercity_app/minicat5.html')


def minicat6(request):
    return render(request, 'papercity_app/minicat6.html')


def minicat7(request):
    return render(request, 'papercity_app/minicat7.html')


def minicat8(request):
    return render(request, 'papercity_app/minicat8.html')


def minicat9(request):
    return render(request, 'papercity_app/minicat9.html')


def minicat10(request):
    return render(request, 'papercity_app/minicat10.html')


def minicat11(request):
    return render(request, 'papercity_app/minicat11.html')


def minicat12(request):
    return render(request, 'papercity_app/minicat12.html')


def minicat13(request):
    return render(request, 'papercity_app/minicat13.html')


def minicat14(request):
    return render(request, 'papercity_app/minicat14.html')


def minicat15(request):
    return render(request, 'papercity_app/minicat15.html')


def minicat16(request):
    return render(request, 'papercity_app/minicat16.html')


def minicat17(request):
    return render(request, 'papercity_app/minicat17.html')


def minicat18(request):
    return render(request, 'papercity_app/minicat18.html')


def minicat19(request):
    return render(request, 'papercity_app/minicat19.html')


def minicat20(request):
    return render(request, 'papercity_app/minicat20.html')


def minicat21(request):
    return render(request, 'papercity_app/minicat21.html')


def minicat22(request):
    return render(request, 'papercity_app/minicat22.html')


def minicat23(request):
    return render(request, 'papercity_app/minicat23.html')


def minicat24(request):
    return render(request, 'papercity_app/minicat24.html')


def minicat24(request):
    return render(request, 'papercity_app/minicat24.html')


def minicat25(request):
    return render(request, 'papercity_app/minicat25.html')


def minicat26(request):
    return render(request, 'papercity_app/minicat26.html')


def minicat27(request):
    return render(request, 'papercity_app/minicat27.html')


def minicat28(request):
    return render(request, 'papercity_app/minicat28.html')


def minicat29(request):
    return render(request, 'papercity_app/minicat29.html')


def minicat30(request):
    return render(request, 'papercity_app/minicat30.html')


def minicat31(request):
    return render(request, 'papercity_app/minicat31.html')


def minicat32(request):
    return render(request, 'papercity_app/minicat32.html')


def minicat33(request):
    return render(request, 'papercity_app/minicat33.html')


def minicat34(request):
    return render(request, 'papercity_app/minicat34.html')


def minicat35(request):
    return render(request, 'papercity_app/minicat35.html')


def minicat36(request):
    return render(request, 'papercity_app/minicat36.html')


def minicat37(request):
    return render(request, 'papercity_app/minicat37.html')


def minicat38(request):
    return render(request, 'papercity_app/minicat38.html')


def minicat39(request):
    return render(request, 'papercity_app/minicat39.html')


def minicat40(request):
    return render(request, 'papercity_app/minicat40.html')


def minicat41(request):
    return render(request, 'papercity_app/minicat41.html')


def minicat42(request):
    return render(request, 'papercity_app/minicat42.html')


def minicat43(request):
    return render(request, 'papercity_app/minicat43.html')


def minicat44(request):
    return render(request, 'papercity_app/minicat44.html')


def minicat45(request):
    return render(request, 'papercity_app/minicat45.html')
