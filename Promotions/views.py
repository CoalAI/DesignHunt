"""
Promotions/views.py
Authors:
"""
from rest_framework import generics

from Promotions.models import Promotion
from Promotions.serializes import PromotionSerializer


class PromotionViewSet(generics.ListAPIView):
    """
    RestInterface.v2.views.OrderDoughnutViewSet
    """
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()
