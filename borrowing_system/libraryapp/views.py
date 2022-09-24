from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book

def index(request):
    books = Book.objects.all()
    template = loader.get_template('bookesimerkki.html')
    context = {
        'books' : books
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
