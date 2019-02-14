from apis.serializers import UserSerializer
from calendar import timegm
from rest_framework_jwt.settings import api_settings
from django.conf import settings
import datetime


def jwt_payload_handler(user):
    """ Custom payload handler
    Token encrypts the dictionary returned by this function, and can be decoded by rest_framework_jwt.utils.jwt_decode_handler
    """
    return {
        'user_id': user.pk,
        'email': user.email,
        'is_superuser': user.is_superuser,
        'exp': datetime.datetime.now().replace(microsecond=0) + api_settings.JWT_EXPIRATION_DELTA,
        'orig_iat': timegm(
            datetime.datetime.now().timetuple()
        )
    }

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        # 'user': UserSerializer(user, context={'request': request}).data,
        'exp': datetime.datetime.now().replace(microsecond=0) + api_settings.JWT_EXPIRATION_DELTA,
        'orig_iat': timegm(
            datetime.datetime.now().timetuple()
        )
    }
