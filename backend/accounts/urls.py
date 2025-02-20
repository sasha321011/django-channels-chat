from rest_framework.routers import DefaultRouter
from .views import Registration, Login

router = DefaultRouter()
router.register(r"registration", Registration, basename="registration")
router.register(r"login", Login, basename="login")
urlpatterns = router.urls
