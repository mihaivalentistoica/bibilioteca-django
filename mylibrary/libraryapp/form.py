from django import forms

from .models import Book, Student


class BorrowForm(forms.Form):
    book = forms.ChoiceField(label="Carte", choices=[(b.id, b.name) for b in Book.objects.all()], required=True)
    student = forms.ChoiceField(label="Student", choices=[(s.id, s.name) for s in Student.objects.all()], required=True)
    return_date = forms.DateField(label="Data de retur", widget=forms.SelectDateWidget())
