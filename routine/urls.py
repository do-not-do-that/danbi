from rest_framework import routers
from .views import RoutineCreateAPIView, RoutineDetailAPIView
from django.urls import path, include


urlpatterns = [
    path('', RoutineCreateAPIView.as_view()),
    path('<int:pk>', RoutineDetailAPIView.as_view()),
]