"""
Promotions/views.py
Authors:
"""
from rest_framework import generics

from promotions.models import MailGun, Promotion
from promotions.serializes import MailGunSerializer, PromotionSerializer


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


class MailGunViewSet(generics.ListCreateAPIView):
    """
    RestInterface.v2.views.OrderDoughnutViewSet
    """
    serializer_class = MailGunSerializer
    queryset = MailGun.objects.all()

    def perform_create(self, serializer):
        print(serializer)
        # return super().perform_create(serializer)
        serializer.save()  # author=self.request.user)
