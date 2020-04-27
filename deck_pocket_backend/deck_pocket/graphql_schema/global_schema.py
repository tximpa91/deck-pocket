import graphene
from .card.card_schema import CardSchema
from deck_pocket.models import Card


class Query(graphene.ObjectType):
    all_cards = graphene.List(CardSchema)
    card = graphene.List(CardSchema, card_name=graphene.String(), distinct=graphene.Boolean())

    def resolve_all_cards(self, info):
        return Card.objects.all()[:10]

    def resolve_card(self, info, card_name, **kwargs):
        distinct = kwargs.get('distinct')
        queryset = Card.objects.filter(name__icontains=card_name)
        if distinct:
            return queryset.distinct('name')
        return queryset
