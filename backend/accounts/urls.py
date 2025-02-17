from rest_framework.routers import DefaultRouter
from .views import Registration

router = DefaultRouter()
router.register(r"registration", Registration, basename="registration")

urlpatterns = router.urls


