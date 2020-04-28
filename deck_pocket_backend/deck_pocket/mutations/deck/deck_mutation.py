from graphene import Mutation, String, Field, List
from deck_pocket.graphql_schema.deck.deck_schema import DeckSchema
from deck_pocket.models import Card, Deck
from django.db import transaction


class CreateDeck(Mutation):
    class Input:
        # The input arguments for this mutation
        name = String(required=True)
        deck_type = String(required=True)
        cards = List(String)

    # The class attributes define the response of the mutation
    deck = Field(DeckSchema)

    @transaction.atomic
    def mutate(self, info, name, deck_type, cards, **kwargs):
        user = kwargs.pop('user')
        cards = Card.get_cards(cards)
        deck = Deck(name=name, deck_type=deck_type, user_deck=user)
        deck.save()
        for card in cards:
            deck.cards.add(card)
        return CreateDeck(deck=deck)
