# Create your views here.
from django.shortcuts import render
from mysite.books.models import Book 


def booklist(request):
    books = Book.objects.order_by('title')
    return render(request, 'search_results.html', {'books': books, 'query': 'todos'})
