from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import AddboardsConfig
from .views import AdViewSet, ReviewViewSet

app_name = AddboardsConfig.name

router = DefaultRouter()
router.register(r"ads", AdViewSet)
router.register(r"reviews", ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
