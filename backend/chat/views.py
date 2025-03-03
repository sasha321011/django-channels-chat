from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from django.contrib.auth import get_user_model
from .serializers import UserGetSerializer

User = get_user_model()
class ListUser(GenericViewSet,mixins.ListModelMixin):
    serializer_class = UserGetSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = User.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.exclude(id=self.request.user.id)

        return queryset