# Projeto django + rest + react
Criado a partir de: https://www.valentinog.com/blog/drf/

## Testar todos os códigos próprios adicionados na aplicação
```coverage run --source='.' manage.py test && coverage html```

## Migrar novos modelos
```python manage.py makemigrations && python manage.py migrate```

## Dependências
Gerar:

```pip freeze > requirements.txt```

Restaurar:

```pip install -r requirements.txt```

## Criar novo REST
* Criar app:
```
python manage.py startapp app
```

* Criar o arquivo 'models.py':
```
from django.db import models

class Modelo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
```
* Migrar o modelo
```
python manage.py makemigrations
python manage.py migrate
```
* Criar serializador para conversão entre objetos JSON e Python:
```
from rest_framework import serializers
from .models import Modelo

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('id', 'name', 'email', 'message')
```
* Criar a view(o exemplo utiliza 'generic API view', tratando requisições GET e POST) para retornar e criar objetos quando uma requisição for recebida:
```
from .models import Modelo
from .serializers import ModeloSerializer
from rest_framework import generics

class ModeloListCreate(generics.ListCreateAPIView):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
```
* Adicionar a view no roteamento de URLs do arquivo 'urls.py' do projeto:
```
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
]
```
* Criar o arquivo 'urls.py' na pasta do app:
```
from django.urls import path
from . import views

urlpatterns = [
    path('api/app/', views.ModeloListCreate.as_view() ),
]
```
* Adicionar o framework rest no arquivo 'settings.py':
```
INSTALLED_APPS = [
    'leads.apps.LeadsConfig',
    'rest_framework',
]
```

## settings.py de produção
Desabilitar o navegador de API:
```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
```
Desabiltar o DEBUG:
```
DEBUG = False
```
