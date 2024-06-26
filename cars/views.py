from django.shortcuts import render, get_object_or_404
from .models import Cars
from django.views import View
from .serializer import CarsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView



class CarsListApiView(ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class CarsRetrieveApiView(RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer



class CarsAPIView(APIView):
    def get(self, request):
        cars = Cars.objects.values()
        return Response(cars)
