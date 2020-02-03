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

    def get_queryset(self):
        hostname = self.request.query_params.get('hostname') or None
        if hostname:
            return MailGun.objects.filter(domain__icontains=hostname)
        return []

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.capital_from = self.request.data['From']
        instance.from_from = self.request.data['from']
        instance.x_envelope_from = self.request.data['X-Envelope-From']
        instance.subject_subject = self.request.data['Subject']
        instance.x_google_dkim_signature = self.request.data['X-Google-Dkim-Signature']
        instance.to_to = self.request.data['To']
        instance.dkim_signature = self.request.data['Dkim-Signature']
        instance.x_received = self.request.data['X-Received']
        instance.date_date = self.request.data['Date']
        instance.message_id = self.request.data['Message-Id']
        instance.mime_version = self.request.data['Mime-Version']
        instance.received_received = self.request.data['Received']
        instance.message_url = self.request.data['message-url']
        instance.x_mailgun_incoming = self.request.data['X-Mailgun-Incoming']
        instance.x_gm_message_state = self.request.data['X-Gm-Message-State']
        instance.message_headers = self.request.data['message-headers']
        instance.content_type = self.request.data['Content-Type']
        instance.x_google_smtp_source = self.request.data['X-Google-Smtp-Source']
        instance.subject_subject = self.request.data['Subject']
        instance.body_plain = self.request.data['body-plain']
        instance.body_html = self.request.data['body-html']
        instance.stripped_text = self.request.data['stripped-text']
        instance.stripped_html = self.request.data['stripped-html']
        instance.save()  # author=self.request.user)
