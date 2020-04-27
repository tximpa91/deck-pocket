from graphene_django import DjangoObjectType
from deck_pocket.models import Card
import graphene


class CardSchema(DjangoObjectType):
    class Meta:
        model = Card



