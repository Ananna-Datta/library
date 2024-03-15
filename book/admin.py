from django.contrib import admin
from book.models import Book,BorrowedBook,Comment

# Register your models here.
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(Comment)