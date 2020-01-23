"""
Promotions/views.py
Authors:
"""
from rest_framework import generics

from promotions.models import Promotion
from promotions.serializes import PromotionSerializer


class PromotionViewSet(generics.ListAPIView):
    """
    RestInterface.v2.views.OrderDoughnutViewSet
    """
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()
