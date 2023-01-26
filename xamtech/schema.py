import graphene
import films.schema

class Query(films.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)