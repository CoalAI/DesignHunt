"""
Doc string needed here
"""
from django.urls import path

from Promotions.views import PromotionViewSet

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('promotion/', PromotionViewSet.as_view()),
]
