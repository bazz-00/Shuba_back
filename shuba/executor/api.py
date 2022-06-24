from .models import Executor, Speciality, ExecutorComments
from rest_framework import viewsets, permissions
from .serializers import ExecutorSerializer, SpecialitySerializer, ExecutorCommentsSerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExecutorSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SpecialitySerializer


class ExecutorCommentsViewSet(viewsets.ModelViewSet):
    queryset = ExecutorComments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExecutorCommentsSerializer


