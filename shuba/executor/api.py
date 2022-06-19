from .models import Executor
from rest_framework import viewsets, permissions
from .serializers import ExecutorSerializer

class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExecutorSerializer