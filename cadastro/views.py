from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .models import Caminhao
from .serializers import CaminhaoSerializer, UserSerializer
from rest_framework import generics


class CaminhaoListCreate(generics.ListCreateAPIView):
    queryset = Caminhao.objects.all()
    serializer_class = CaminhaoSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
