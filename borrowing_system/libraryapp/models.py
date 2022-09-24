from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name
    #Ja muita kenttiä edelleen...
class Book(models.Model):
    name = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
    #Ja muita kenttiä edelleen....

# Create your models here.

#Kun kenttiä (tai malleja lisätään edelleen) täytyy tehdä komentorivin kautta tehdä uusi migraatio, 
#jotta kentät (tai taulut) saadaan siirrettyä tietokantaan.