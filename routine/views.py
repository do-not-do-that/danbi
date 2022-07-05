from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Routine
from .serializers import RoutineSerializer


class RoutineCreateAPIView(generics.CreateAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class RoutineDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

