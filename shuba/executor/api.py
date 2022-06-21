from .models import Executor, Speciality, Orders
from rest_framework import viewsets, permissions
from .serializers import ExecutorSerializer, SpecialitySerializer, OrdersSerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExecutorSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SpecialitySerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrdersSerializer
