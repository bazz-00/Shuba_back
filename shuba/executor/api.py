from .models import Executor, Speciality
from rest_framework import viewsets, permissions
from .serializers import ExecutorSerializer, SpecialitySerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExecutorSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SpecialitySerializer
