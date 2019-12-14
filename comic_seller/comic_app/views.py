from django.shortcuts import render
from comic_app.models import Books
from comic_app.forms import BooksForm


# Create your views here.


def get_all_books(request):
    book_list = Books.objects.all()
    return render(request, 'landing_page.html', {'form': BooksForm})
