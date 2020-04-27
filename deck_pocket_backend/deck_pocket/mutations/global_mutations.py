import graphene
from .deck.deck_mutation import CreateDeck


class Mutation(graphene.ObjectType):
    create_deck = CreateDeck.Field()
