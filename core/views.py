import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from drfpasswordless.views import ObtainAuthTokenFromCallbackToken


logger = logging.getLogger(__name__)

class CustomObtainAuthTokenFromCallbackToken(ObtainAuthTokenFromCallbackToken):
    """
    This is a customtomization for ObtainAuthTokenFromCallbackToke of passwordless.
    this returns a JWT based on our 6 digit callback token and source.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]

            
            access_token = AccessToken.for_user(user=user)
            refresh_token = RefreshToken.for_user(user=user)
            return Response({'access': str(access_token),
                            'refresh': str(refresh_token)},
                            status=status.HTTP_200_OK)
        else:
            logger.error("Couldn't log in unknown user. Errors on serializer: {}".format(serializer.error_messages))
        return Response({"detail": "Couldn't log you in. Try again later."}, status=status.HTTP_400_BAD_REQUEST)
    



