import graphene
from graphene_django import DjangoObjectType
import books.schema


class Query(books.schema.Query, graphene.ObjectType):
    """各Appで実装したクエリでスキーマを作成する"""


schema = graphene.Schema(query=Query)
