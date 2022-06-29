import strawberry
import app.schema
from strawberry_django_plus.optimizer import DjangoOptimizerExtension


class Query(app.schema.Query):
    pass


class Mutation(app.schema.Mutation):
    pass


schema = strawberry.Schema(query=Query,
                           mutation=Mutation,
                           extensions=[DjangoOptimizerExtension])


