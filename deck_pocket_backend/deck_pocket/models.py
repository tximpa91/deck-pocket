from django.db import models
from django.contrib.auth.models import AbstractUser
from oauth2_provider.models import AbstractApplication
from firebase_admin import initialize_app


# Create your models here.


class Oauth2ProviderDeckPocket(AbstractApplication):
    scopes = models.CharField(blank=True, null=True, max_length=255)

    def allows_grant_type(self, *grant_types):
        # Assume, for this example, that self.authorization_grant_type is set to self.GRANT_AUTHORIZATION_CODE

        return bool(set([self.authorization_grant_type, self.GRANT_CLIENT_CREDENTIALS, ]) & set(grant_types))

    class Meta:
        verbose_name_plural = "OAuth2 Applications"


class DeckPocketUser(models.Model):
    uid = models.CharField(max_length=255, db_column='Uid', db_index=True)

    class Meta:
        db_table = 'DeckPocketUser'
