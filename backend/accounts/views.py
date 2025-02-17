from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class Registration(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model()

