from ..models import LoanableBook
from django.core.exceptions import BadRequest
def loan_book(loanable_book_id, user_id):
    book = LoanableBook.objects.get(id=loanable_book_id)
    if book.available():
        book.loan(user_id)
    else:
        raise BadRequest("Virhe. Jo lainattua kirjaa ei pystytty lainaamaan.")
def return_book(loanable_book_id, user_id):
    book = LoanableBook.objects.get(id=loanable_book_id)