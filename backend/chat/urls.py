from django.urls import path
from rest_framework.routers import DefaultRouter
from .consumers import PersonalChatConsumer
from .views import ListUser

router = DefaultRouter()


websocket_urlpatterns = [
    path('ws/chat/',PersonalChatConsumer.as_asgi()),
]

urlpatterns = [
]


router.register(r"users", ListUser, basename="user_list")

urlpatterns = router.urls

