from rest_framework import serializers
from .models import Caminhao


class CaminhaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caminhao
        fields = ('id', 'modelo', 'marca', 'placa', 'ano')
