from django.urls import path, include
from profiller.api.views import ProfilViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiller',ProfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]