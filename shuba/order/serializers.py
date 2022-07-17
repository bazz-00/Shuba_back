from rest_framework import serializers

from .models import Order, OrderComments, OrderPhotos, SpecialityOrder


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SpecialityOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialityOrder
        fields = '__all__'


class OrderCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderComments
        fields = '__all__'


class OrderPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPhotos
        fields = '__all__'

