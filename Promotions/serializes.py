"""
serializers.py
Authers: 
Reviewed by: 
RestInterface Serializers Configuration

For more information please see:
    https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

ModelSerializer
    1. Extend serializers.ModelSerializer from rest_framework:
    class AbcSerializer(serializers.ModelSerializer):
    2. Add a Meta class:  class Meta:
    3. Meta class required 2 variable to override
        a. Model
        b. fields

    Examples:
    class AbcSerializer(serializers.ModelSerializer):
        class Meta:
            model = Abc
            fields = '__all__'

"""
import datetime
import json

from django.db import models
from rest_framework import serializers

from Authentication.models import User
from Promotions.models import Promotion


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer use is_manager and is_coordinator ReadOnlyField in case we
    use this is future to edit this model
    """

    class Meta:
        model = User
        fields = ('id', 'username',)


class PromotionSerializer(serializers.ModelSerializer):
    """
    ProjectSmallSerializer only contain following fields
    id, customer, manager, project_code,
    """
    class Meta:
        model = Promotion
        fields = '__all__'
