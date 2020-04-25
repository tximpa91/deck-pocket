from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.conf import settings
from firebase_admin import auth
from deck_pocket.models import DeckPocketUser


class FireBaseAuth(BasePermission):

    def __init__(self):
        self.firebase_app = settings.FIREBASE_APP

    def validate_firebase_user(self, headers):
        try:
            if 'Firebase-User' in headers:
                uid = headers.get('Firebase-User')
                if DeckPocketUser.user_exists(uid):
                    return True
                else:
                    user = auth.get_user(uid)
                    return DeckPocketUser().create_or_login(user.uid)
            return False

        except Exception as error:
            return False

    def has_permission(self, request, view):
        return self.validate_firebase_user(request.headers)
