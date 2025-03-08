"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from chat.urls import websocket_urlpatterns
from chat.channels_middleware import JWTWebsocketMiddleware
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'http':application,
    'websocket':JWTWebsocketMiddleware(AuthMiddlewareStack(URLRouter(websocket_urlpatterns)))
})