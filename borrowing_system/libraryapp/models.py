from contextlib import nullcontext
from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.last_name + "," + self.first_name
class Book(models.Model):
    name = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author, on_delete=models.PROTECT)
    release_date = models.DateField(null = True)
    ISBN_code = models.CharField(max_length=17, null = True)
    def __str__(self):
        return self.name
class LoanableBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.ForeignKey(User, on_delete=models.PROTECT, null = True)
    loan_date = models.DateField(null = True)
    due_date = models.DateField(null = True)
    def return_book(self, user_id):
        if self.borrower == None or self.borrower != user_id:
            raise ValidationError("Virhe tapahtui, toimintoa ei voitu suorittaa.")
        self.borrower = None
    def loan(self, user_id):
        self.borrower = user_id
        self.loan_date = date.today()
        self.due_date = date.today() + timedelta(weeks=4)
    def available(self):
        return self.borrower == None
    def days_left(self):
        return (date.today() - self.due_date).days