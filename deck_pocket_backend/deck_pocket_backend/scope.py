from oauth2_provider.scopes import BaseScopes
from oauth2_provider.settings import oauth2_settings


class CustomScopes(BaseScopes):
    def get_all_scopes(self):
        print(oauth2_settings.SCOPES)
        return oauth2_settings.SCOPES

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        print(application.scopes.split(";"))
        return application.scopes.split(";")

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        print(application.scopes.split(";"))
        return application.scopes.split(";")
