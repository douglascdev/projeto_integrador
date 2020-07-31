from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Caminhao


class CaminhaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caminhao
        fields = ('id', 'modelo', 'marca', 'placa', 'ano')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user