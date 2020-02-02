"""
Doc string needed here
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Promotion(models.Model):
    """
    Promotion Model create in database
    """
    MEDIUM_CHOICES = (
        ('MEDIUM_FB', 'Facebook'),
        ('MEDIUM_EMAIL', 'Email'),
    )

    company_name = models.CharField(_('Company name'), max_length=256)
    company_domain = models.CharField(_('Company Domain'), max_length=256)
    email_from = models.EmailField(_('Email From'), max_length=256, null=True, blank=True)
    email_to = models.EmailField(_('Email To'), max_length=256, null=True, blank=True)
    promotion_heading = models.CharField(_('Promotion Subject'), max_length=256)
    promotion_url = models.URLField(null=True, blank=True)
    promotion_type = models.CharField(_('Promotion Type'), max_length=100)
    content = models.TextField(_('HTML Email'))
    email_mobile = models.URLField(null=True, blank=True)
    email_desktop = models.URLField(null=True, blank=True)
    techknowlogy = models.CharField(_('Email powered by'), max_length=64, null=True, blank=True)
    medium = models.CharField(_('Medium'), default='MEDIUM_FB', choices=MEDIUM_CHOICES, max_length=64)
    recieved_at = models.DateTimeField(null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.promotion_heading
