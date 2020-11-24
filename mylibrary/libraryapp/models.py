from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    number_of_page = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    stock_quantity = models.IntegerField(default=1)
    isbn = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICE = [
        (1, 'First year'),
        (2, 'Second year'),
        (3, 'Third year'),
        (4, 'Forth year'),
    ]
    name = models.CharField(max_length=100)
    school_year = models.IntegerField(choices=YEAR_IN_SCHOOL_CHOICE, default=1)
    birth_date = models.DateField(null=True, blank=True)
    books = models.ManyToManyField(Book, through="Borrow")

    def __str__(self):
        return self.name


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now=True)
    return_date = models.DateField()
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student} borrowed {self.book}'
