import graphene
from .deck.deck_mutation import CreateOrUpdateDeck


class Mutation(graphene.ObjectType):
    create_or_update_deck = CreateOrUpdateDeck.Field()
