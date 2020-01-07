"""
Promotions/models.py
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

MEDIUM_CHOICES = (
    ('fb', 'Facebook'),
    ('email', 'Email'),
)

class Promotion(models.Model):
    """
    Promotion Model create in database
    """
    company_name = models.CharField(_('Company name'), max_length=256)
    company_domain = models.CharField(_('Company Domain'), max_length=256)
    email_from = models.EmailField(_('Email From'), max_length=256, null=True, blank=True)
    email_to = models.EmailField(_('Email To'), max_length=256, null=True, blank=True)
    promotion_heading = models.CharField(_('Promotion Subject'), max_length=256)
    promotion_url = models.URLField(null=True, blank=True)
    promotion_type = models.CharField(_('Role'), max_length=100)
    content = models.TextField()
    promotion_snap = models.URLField()
    medium = models.CharField(_('Medium'), default='fb', choices=MEDIUM_CHOICES, max_length=64)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.promotion_subject
