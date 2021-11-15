import graphene
from graphene_django import DjangoObjectType
from .models import Book, Author
from typing import Optional


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
        title=graphene.String(
            required=False,
            description="書籍名"
        ),
        description="書籍一覧取得API"
    )

    def resolve_books(root, info, title: Optional[str] = None):
        qs = Book.objects.all()
        if title:
            qs = qs.filter(title__contains=title)
        return qs

