from django.urls import include, path
from rest_framework.routers import SimpleRouter

from erp_backend.apps.nomenclators.cod_currency.views import CurrencyViewSet

router = SimpleRouter()
router.register("Currency", CurrencyViewSet, basename="currency")

versioned_urls = [path("", include(router.urls))]
