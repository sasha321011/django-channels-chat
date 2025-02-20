from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer
from .tokenauthentication import JWTAuthentication


class Registration(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class Login(GenericViewSet):
    serializer_class = LoginSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            token = JWTAuthentication.generate_token(payload=serializer.data)
            return Response(
                {
                    "message": "Login Successful",
                    "token": token,
                    "user": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)