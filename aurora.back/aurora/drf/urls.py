from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AddressBalanceView,
    AddressNonceView,
    BlockViewset,
    TransactionViewset,
)

app_name = "drf"

router = DefaultRouter()
router.register(r"block", BlockViewset, basename="block")
router.register(r"transaction", TransactionViewset, basename="transaction")

urlpatterns = [
    path("", include(router.urls)),
    path("address_nonce/<slug:address>", AddressNonceView.as_view()),
    path("address_balance/<slug:address>", AddressBalanceView.as_view()),
]
