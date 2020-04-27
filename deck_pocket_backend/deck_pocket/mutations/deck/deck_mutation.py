from graphene import Mutation, String, Field
from deck_pocket.graphql_schema.deck.deck_schema import DeckSchema


class CreateDeck(Mutation):
    class Input:
        # The input arguments for this mutation
        name = String(required=True)
        deck_type = String(required=True)

    # The class attributes define the response of the mutation
    deck = Field(DeckSchema)

    def mutate(self, info, name, deck_type, **kwargs):
        print(kwargs)
        return
