import graphene
from graphene_django import DjangoObjectType
from .models import Book, Author
from typing import Optional
from graphql import GraphQLError


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


class NewAuthorInput(graphene.InputObjectType):
    """作者登録の入力型"""
    first_name= graphene.String(
        required=True, description="名"
    )
    last_name = graphene.String(
        required=True, description="姓"
    )


class NewBookInput(graphene.InputObjectType):
    """書籍登録の入力型"""
    title = graphene.String(
        required=True, description="タイトル"
    )
    author = NewAuthorInput(
        required=True, description="作者"
    )


class NewBookMutation(graphene.Mutation):
    """書籍登録ミューテーション"""
    class Arguments:
        book = NewBookInput(required=True)

    class Meta:
        output = graphene.NonNull(BookType)

    @classmethod
    def mutate(cls, root, info, book: NewBookInput):
        """書籍登録のビジネスロジックを書く場所"""
        raise GraphQLError(
            "未実装です。",
            # デバッグ情報はextensionsに渡す
            extensions={"code": "UNIMPLEMENTED"}
        )
        # 書籍を取得or作成する
        new_book, created = Book.objects.get_or_create(
            title=book["title"]
        )
        author, _ = Author.objects.get_or_create(
            **book["author"]
        )
        new_book.save()
        # BookAuthorの中間レコードを作成する
        new_book.authors.add(author)
        return new_book


class Mutation:
    register_book = NewBookMutation.Field()
