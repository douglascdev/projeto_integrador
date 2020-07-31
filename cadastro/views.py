from .models import Caminhao
from .serializers import CaminhaoSerializer
from rest_framework import generics


class CaminhaoListCreate(generics.ListCreateAPIView):
    queryset = Caminhao.objects.all()
    serializer_class = CaminhaoSerializer
