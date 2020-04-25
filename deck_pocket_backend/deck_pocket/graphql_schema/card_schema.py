from graphene_django import DjangoObjectType
from deck_pocket.models import Card
import graphene


class CardSchema(DjangoObjectType):
    class Meta:
        model = Card


class Query(graphene.ObjectType):
    all_cards = graphene.List(CardSchema)
    card = graphene.List(CardSchema, card_name=graphene.String())

    def resolve_all_cards(self, info):
        return Card.objects.all()[:10]

    def resolve_card(self, info, card_name):
        return Card.objects.filter(name__icontains=card_name)


schema = graphene.Schema(query=Query)
