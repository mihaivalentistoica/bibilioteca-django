from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .form import BorrowForm
from .models import Borrow, Book, Student


def index(req):
    context = {
        'username': 'Adela'
    }
    return render(req, template_name='index.html', context=context)


def return_book(request, pk):
    borrow = Borrow.objects.get(id=pk)
    borrow.is_returned = True
    borrow.save()
    borrow.book.stock_quantity += 1
    borrow.book.save()

    return redirect('borrows_list')


def borrow_book(req):
    if req.method == 'POST':
        form = BorrowForm(req.POST)
        if form.is_valid():
            book = Book.objects.get(id=form.cleaned_data['book'])
            if book.stock_quantity > 0:
                student = Student.objects.get(id=form.cleaned_data['student'])
                Borrow.objects.create(book=book, student=student, return_date=form.cleaned_data['return_date'])
                book.stock_quantity -= 1
                book.save()
                return redirect('borrows_list')
    else:
        form = BorrowForm()
    return render(req, template_name='create_borrow.html', context={'form': form})


class BorrowView(ListView):
    model = Borrow
    template_name = 'borrow_list.html'
