from django.shortcuts import render
from .models import Book
# Create your views here.

def home(request):
    context = {
    'books': Book.objects.all()
    }
    return render(request, 'books/home.html', context=context)
def detail(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'books/detail.html', context=context)