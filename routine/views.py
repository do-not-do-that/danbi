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

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)

    #     resp = {
    #         "data" : {
    #             "routine_id": serializer.data['id']
    #         },
    #         "message" : {
    #             "msg": " .",
    #             "status": "ROUTINE_CREATE_OK"
    #         }
    #     }

    #     return Response(resp, status=status.HTTP_201_CREATED, headers=headers)


class RoutineDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

