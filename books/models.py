from django.db import models


# Create your models here.

class Author(models.Model):
    """作者"""
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    books = models.ManyToManyField("Book", through="BookAuthor")


class Book(models.Model):
    """書籍"""
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author, through="BookAuthor")


class BookAuthor(models.Model):
    """書籍-作者中間テーブル"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    