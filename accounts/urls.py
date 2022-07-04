from rest_framework import routers
from accounts.views import UserViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]