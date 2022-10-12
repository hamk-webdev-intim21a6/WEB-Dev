from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Book, LoanableBook
from django.contrib.auth.models import User

def index(request):
    template = loader.get_template('book_index.html')
    return HttpResponse(template.render({}, request))
# Create your views here.
def books_list(request):
    books = Book.objects.all()
    template = loader.get_template('book_list.html')
    context = {
        'books' : books
    }
    return HttpResponse(template.render(context, request))
def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    template = loader.get_template('book_detail.html')
    return HttpResponse(template.render({'book': book},request))
def loans_list(request):
    loans = LoanableBook.objects.all()
    current_user = User.objects.get(pk = request.user.id)
    user_loans = loans.filter(borrower = current_user)
    template = loader.get_template('loan_list.html')
    return HttpResponse(template.render({'loans' : user_loans}, request))
def loan_detail(request, id):
    loan = get_object_or_404(LoanableBook, pk=id)
    template = loader.get_template('loan_detail.html')
    return HttpResponse(template.render({'loan': loan},request))

def book_loan(request, id):
    book = get_object_or_404(Book, pk=id)
    result = book.loan_available_instance(request.user.id)
    return HttpResponseRedirect(reverse('loan', args={result}))
def return_loan(request, id):
    loaned_book = get_object_or_404(LoanableBook, pk=id)
    loaned_book.return_book()
    return HttpResponseRedirect(reverse('loans'))