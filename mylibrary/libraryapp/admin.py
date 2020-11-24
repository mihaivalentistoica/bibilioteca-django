from django.contrib import admin
from .models import Author, Book, Borrow, Student


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'author', 'stock_quantity', 'number_of_page')
    search_fields = ('name',)


class BookInlineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInlineAdmin
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register([Borrow, Student])
