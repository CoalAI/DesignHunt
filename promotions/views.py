"""
Promotions/views.py
Authors:
"""
from rest_framework import generics

from promotions.models import Promotion
from promotions.serializes import PromotionSerializer


class PromotionViewSet(generics.ListCreateAPIView):
    """
    RestInterface.v2.views.OrderDoughnutViewSet
    """
    serializer_class = PromotionSerializer

    def get_queryset(self):
        hostname = self.request.query_params.get('hostname') or None
        if hostname:
            return Promotion.objects.filter(company_domain=hostname)
        return []
