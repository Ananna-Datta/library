from django.contrib import admin
from django.urls import path, include
from . import views
from book.views import BookBorrowView,BorrowBookListView,BookReturnView
urlpatterns = [
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
     path('borrow_book/<int:id>/', BookBorrowView.as_view(), name='borrow_book'),
    path('borrow_book_lists/', BorrowBookListView.as_view(), name='borrow_book_lists'),
    path('return_book/<int:id>/', BookReturnView.as_view(), name='return_book'),  
]