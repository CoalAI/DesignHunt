"""
Doc string needed here
"""
from django.urls import path

from promotions.views import MailGunViewSet, PromotionViewSet

urlpatterns = [
    path('promotion/', PromotionViewSet.as_view()),
    path('callback/', MailGunViewSet.as_view()),
]
