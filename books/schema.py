import graphene
from graphene_django import DjangoObjectType
from .models import Book, Author


class BookType(DjangoObjectType):
    """書籍の型"""

    class Meta:
        model = Book


class AuthorType(DjangoObjectType):
    """作者の型"""

    class Meta:
        model = Author


class Query:
    # booksクエリのインターフェース(
    books = graphene.Field(
        graphene.List(
            graphene.NonNull(BookType),
            required=True
        ),
        description="書籍取得API"
    )

    def resolve_books(root, info):
        """booksクエリのビジネスロジックを書く場所"""
        return Book.objects.all()
