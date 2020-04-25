from django.db import models
from oauth2_provider.models import AbstractApplication
from django.contrib.postgres.fields import JSONField
import uuid
from django.utils import timezone


# Create your models here.


class DefaultDate(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True, db_column='updated')

    class Meta:
        abstract = True


class Oauth2ProviderDeckPocket(AbstractApplication):
    scopes = models.CharField(blank=True, null=True, max_length=255)

    def allows_grant_type(self, *grant_types):
        # Assume, for this example, that self.authorization_grant_type is set to self.GRANT_AUTHORIZATION_CODE

        return bool(set([self.authorization_grant_type, self.GRANT_CLIENT_CREDENTIALS, ]) & set(grant_types))

    class Meta:
        verbose_name_plural = "OAuth2 Applications"


class DeckPocketUser(DefaultDate):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.CharField(max_length=255, db_column='Uid', db_index=True)

    @staticmethod
    def user_exists(uid=None):
        try:
            DeckPocketUser.objects.get(uid=uid)
            return True
        except Exception as error:
            return False


    @staticmethod
    def create_or_login(uid=None):
        try:
            DeckPocketUser.objects.get_or_create(uid=uid)
            return True
        except Exception as error:
            return False

    class Meta:
        db_table = 'DeckPocketUser'


class Card(DefaultDate):
    card_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.UUIDField(editable=False, blank=True, null=True)
    oracle_id = models.UUIDField(editable=False, blank=True, null=True)
    name = models.CharField(db_column='name', max_length=255, blank=True, null=True)
    uri = models.URLField(max_length=500, blank=True, null=True)
    scryfall_uri = models.URLField(max_length=500, blank=True, null=True)
    image_uris = JSONField(blank=True, null=True)
    mana_cost = models.CharField(max_length=255, blank=True, null=True)
    cmc = models.IntegerField(blank=True, null=True)
    colors = JSONField(blank=True, null=True)
    type_line = models.CharField(max_length=255, blank=True, null=True)
    color_identity = JSONField(blank=True, null=True)
    reserved = models.BooleanField(default=False, blank=True, null=True)
    foil: models.BooleanField(default=False, blank=True, null=True)
    nonfoil = models.BooleanField(default=False, blank=True, null=True)
    promo = models.BooleanField(default=False, blank=True, null=True)
    reprint = models.BooleanField(default=False, blank=True, null=True)
    variation = models.BooleanField(default=False, blank=True, null=True)
    set = models.CharField(db_column='set', max_length=255)
    set_name = models.CharField(db_column='set_name', max_length=255, blank=True, null=True)
    set_type = models.CharField(db_column='set_type', max_length=255, blank=True, null=True)
    set_uri = models.URLField(max_length=500, blank=True, null=True)
    set_search_uri = models.URLField(max_length=500, blank=True, null=True)
    scryfall_set_uri = models.URLField(max_length=500, blank=True, null=True)
    rulings_uri = models.URLField(max_length=500, blank=True, null=True)
    prints_search_uri = models.URLField(max_length=500, blank=True, null=True)
    collector_number = models.CharField(max_length=255, blank=True, null=True)
    digital = models.CharField(max_length=255, blank=True, null=True)
    rarity = models.CharField(max_length=255, blank=True, null=True)
    full_art = models.BooleanField(default=False, blank=True, null=True)
    textless = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = "DeckPocket_Card"


class Deck(DefaultDate):
    deck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(db_column='name', max_length=255, blank=True, null=True)
    user_deck = models.ForeignKey('DeckPocketUser', models.CASCADE,
                                  related_name='deck_user', blank=True, null=True, db_column='user_deck')
    deck_type = models.CharField(max_length=255, blank=True, null=True)
    models.ManyToManyField('Card', db_column='card',
                           db_table='DeckCard')

    class Meta:
        db_table = "Deck"
