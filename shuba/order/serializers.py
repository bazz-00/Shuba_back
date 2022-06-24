from rest_framework import serializers

from .models import Order, OrderComments

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderComments
        fields = '__all__'


