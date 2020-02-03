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


class MailGun(models.Model):
    recipient = models.TextField(null=True, blank=True)
    sender = models.TextField(null=True, blank=True)
    capital_from = models.TextField(null=True, blank=True)
    from_from = models.TextField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    subject_subject = models.TextField(null=True, blank=True)
    body_plain = models.TextField(null=True, blank=True)
    stripped_text = models.TextField(null=True, blank=True)
    stripped_signature = models.TextField(null=True, blank=True)
    body_html = models.TextField(null=True, blank=True)
    stripped_html = models.TextField(null=True, blank=True)
    attachment_count = models.IntegerField(null=True, blank=True)
    attachment_x = models.TextField(null=True, blank=True)
    timestamp = models.IntegerField(null=True, blank=True)
    token = models.TextField(null=True, blank=True)
    signature = models.TextField(null=True, blank=True)
    message_headers = models.TextField(null=True, blank=True)
    content_id_map = models.TextField(null=True, blank=True)
    domain = models.TextField(null=True, blank=True)
    x_envelope_from = models.TextField(null=True, blank=True)
    x_google_dkim_signature = models.TextField(null=True, blank=True)
    to_to = models.TextField(null=True, blank=True)
    dkim_signature = models.TextField(null=True, blank=True)
    x_received = models.TextField(null=True, blank=True)
    date_date = models.TextField(null=True, blank=True)
    message_id = models.TextField(null=True, blank=True)
    mime_version = models.TextField(null=True, blank=True)
    received_received = models.TextField(null=True, blank=True)
    message_url = models.TextField(null=True, blank=True)
    x_mailgun_incoming = models.TextField(null=True, blank=True)
    x_gm_message_state = models.TextField(null=True, blank=True)
    content_type = models.TextField(null=True, blank=True)
    x_google_smtp_source = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.recipient
