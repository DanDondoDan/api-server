from rest_framework import viewsets as views
from api_server import models
from api_server import serializers
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.generics import ListAPIView

class ExchangeViewSet(ListAPIView):
    queryset = models.ExchangeRates.objects.all()
    serializer_class = serializers.ExchangeSerializer
    