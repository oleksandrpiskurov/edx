import requests

from django.contrib.auth.models import User
from django.conf import settings


class UUidBackend:
    """
    Authenticate by given uuid
    """

    def authenticate(self, request, uuid, *args, **kwargs):
        response = requests.post('{0}health-check/validate/'.format(settings.CYBERSMART_API_URL),
                                 data={'uuid': uuid})
        if not response.ok:
            return None
        try:
            return User.objects.get(email=response.json()['email'])
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
