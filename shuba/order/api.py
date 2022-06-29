from .models import Order, OrderComments, OrderPhotos
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer, OrderCommentsSerializer, OrderPhotosSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer


class OrderCommentsViewSet(viewsets.ModelViewSet):
    queryset = OrderComments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderCommentsSerializer


class OrderPhotosViewSet(viewsets.ModelViewSet):
    queryset = OrderPhotos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderPhotosSerializer




