from rest_framework import serializers
from .models import Executor, Speciality, ExecutorComments


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class ExecutorCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutorComments
        fields = '__all__'
