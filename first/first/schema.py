import strawberry
import strawberry_django
from typing import List
from .types import Fruit


@strawberry.type
class Query:
    fruits: List[Fruit] = strawberry_django.field()


schema = strawberry.Schema(query=Query)
