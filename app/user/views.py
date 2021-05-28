from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer


# generics.CreateAPIView has a default site and configuration for a service
# that only creates objects


class CreateUserView(generics.CreateAPIView):

    """Create a new user in the system"""

    serializer_class = UserSerializer


# Generic class that is used to obtain an authentication Token


class CreateTokenView(ObtainAuthToken):

    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer

    # Set the renderer in order to see the API on the browser
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the autheticated user"""

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Return authenticated user"""
        return self.request.user
