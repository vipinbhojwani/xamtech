import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Film

class FilmType(DjangoObjectType):
    class Meta:
        model = Film

class Query(ObjectType):
    film = graphene.Field(FilmType, id=graphene.Int())
    films = graphene.List(FilmType, offset=graphene.Int(), limit=graphene.Int())
    

    def resolve_film(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Film.objects.get(pk=id)

        return None

    def resolve_films(self, info, **kwargs):
        limit = kwargs.get('limit')
        offset = kwargs.get('offset')
        return Film.objects.filter(pk__gte=offset).filter(pk__lt=offset+limit)


schema = graphene.Schema(query=Query)
