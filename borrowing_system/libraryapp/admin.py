from django.contrib import admin

from .models import Book, Author, LoanableBook

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(LoanableBook)
# Register your models here.
