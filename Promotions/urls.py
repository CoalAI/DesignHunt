"""
Doc string needed here
"""
from django.urls import path

from Promotions.views import PromotionViewSet

urlpatterns = [
    path('promotion/', PromotionViewSet.as_view()),
]
