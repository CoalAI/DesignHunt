"""
Doc string needed here
"""
from django.urls import path

from promotions.views import PromotionViewSet

urlpatterns = [
    path('promotion/', PromotionViewSet.as_view()),
]
