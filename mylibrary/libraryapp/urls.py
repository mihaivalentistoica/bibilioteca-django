from django.urls import path

from .views import BorrowView, return_book, borrow_book

urlpatterns = [
    path('', BorrowView.as_view(), name="borrows_list"),
    path('return/<int:pk>', return_book, name="return_book"),
    path('borrow_book', borrow_book, name="borrow_book"),
]
