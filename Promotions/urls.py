"""
Promotions/urls.py
"""
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from Promotions.views import PromotionViewSet

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('promotion/', PromotionViewSet.as_view()),
]
