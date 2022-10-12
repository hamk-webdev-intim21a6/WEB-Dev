from contextlib import nullcontext
from django.db import models
from django.urls import reverse
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.first_name if self.last_name == None else self.last_name + "," + self.first_name
class Book(models.Model):
    name = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author, on_delete=models.PROTECT)
    release_date = models.DateField(null = True)
    ISBN_code = models.CharField(max_length=17, null = True)
    def __str__(self):
        return self.name
    def has_loanable_instance(self):
        instances = LoanableBook.objects.filter(book=self)
        for book_instance in instances:
            if book_instance.available() == True:
                return True
        return False
    def get_absolute_url(self):
        return reverse("book", kwargs={"id": self.pk})
    def loan_available_instance(self, userid):
        instances = LoanableBook.objects.filter(book=self)
        loanable_instance = instances.get(borrower=None)
        loanable_instance.loan(userid)
        loanable_instance.save()
        print(loanable_instance.pk)
        return loanable_instance.pk
    
class LoanableBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.ForeignKey(User, on_delete=models.PROTECT, null = True, blank = True)
    loan_date = models.DateField(null = True, blank = True)
    due_date = models.DateField(null = True, blank = True)

    def return_book(self):
        self.loan_date = None
        self.due_date = None
        self.borrower = None
        self.save()
    def loan(self, user_id):
        user = User.objects.get(pk=user_id)
        self.borrower = user
        self.loan_date = date.today()
        self.due_date = date.today() + timedelta(weeks=4)
    def available(self):
        return self.borrower == None
    def days_left(self):
        return (self.due_date - date.today()).days
    def __str__(self):
        return self.book.name
    def get_absolute_url(self):
        return reverse("loan", kwargs={"id": self.pk})        