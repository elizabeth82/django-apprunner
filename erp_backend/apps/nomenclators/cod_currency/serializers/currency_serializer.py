from rest_framework import serializers

from erp_backend.apps.nomenclators.cod_currency.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"
        read_only_fields = ("id",)
