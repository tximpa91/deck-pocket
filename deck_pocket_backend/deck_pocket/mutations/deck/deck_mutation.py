from graphene import Mutation, String, Field, List
from deck_pocket.graphql_schema.deck.deck_schema import DeckSchema
from deck_pocket.models import Card, Deck, Whishlist, MyCards
from django.db import transaction
from deck_pocket.graphql_fields.custom_fields import DeckDictionary


class CreateOrUpdateDeck(Mutation):
    class Input:
        # The input arguments for this mutation
        deck_id = String(required=False)
        name = String(required=True)
        deck_type = String(required=True)
        cards = List(DeckDictionary)

    # The class attributes define the response of the mutation
    deck = Field(DeckSchema)

    @transaction.atomic
    def mutate(self, info, name, deck_type, **kwargs):
        """Create or update a deck if deck_id is not null if for update"""
        user = kwargs.pop('user')
        deck_id = kwargs.get('deck_id')
        cards = kwargs.get('cards')
        if deck_id is not None:
            deck = Deck.get_deck(deck_id)
            deck.name = name
            deck.deck_type = deck_type
            deck.cards.clear()
            deck.save()
        else:
            deck = Deck(name=name, deck_type=deck_type, user_deck=user)
            deck.save()
        # Associate cards to a deck
        if cards:
            cards_to_find = [card.get('card_id') for card in cards]
            cards_for_create_or_update = Card.get_cards(cards_to_find)
            for card in cards_for_create_or_update:
                deck.cards.add(card)
            wishlist, my_cards = Deck.get_ownership(cards_to_find)

        return CreateOrUpdateDeck(deck=deck)
