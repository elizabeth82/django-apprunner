from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from erp_backend.apps.nomenclators.cod_currency.models import Currency
from erp_backend.apps.nomenclators.cod_currency.serializers import (CurrencySerializer)

class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    http_method_names = ["get", "post", "delete", "put"]
    serializer_class = CurrencySerializer
    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ["name"]
    search_fields = ["code", "name"]
