from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('books', views.books_list, name="books"),
    path('books/<int:id>', views.book_detail, name="book"),
    path('books/<int:id>/loan', views.book_loan, name="loanbook"),
    path('loans', views.loans_list, name="loans"),
    path('loans/<int:id>', views.loan_detail, name="loan"),
    path('loans/<int:id>/return', views.return_loan, name="returnbook")

]