from django.shortcuts import render
from book.models import Book
from categories.models import Category
from transactions.models import Transaction


def home(request, category_slug = None):
    data = Book.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Book.objects.filter(category  = category)
    categories = Category.objects.all()
    transactions = Transaction.objects.all()
    return render(request, 'home.html', {'data' : data, 'category' : categories, 'transactions' : transactions})