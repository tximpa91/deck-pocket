from graphene_django import DjangoObjectType
from deck_pocket.models import Card
import graphene


class CardSchema(DjangoObjectType):
    class Meta:
        model = Card


class Query(graphene.ObjectType):
    all_cards = graphene.List(CardSchema)

    def resolve_all_cards(self, info):
        return Card.objects.all()[:10]


schema = graphene.Schema(query=Query)
