import uuid
from rest_framework import views, permissions, status
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

from rest_framework_jwt.views import ObtainJSONWebToken

# from apis.serializers import JWTSerializer
# Create your views here.


# class ObtainJWTView(ObtainJSONWebToken):
#     serializer_class = JWTSerializer

class SpaUserLogoutAllView(views.APIView):
    """
    Use this endpoint to log out all sessions for a given user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



