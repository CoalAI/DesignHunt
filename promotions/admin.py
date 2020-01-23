"""
RestInterface.admin
"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from promotions.models import Promotion

admin.site.site_header = _('Design Hunt')
admin.site.site_title = _('Design Hunt')


admin.site.register(Promotion)
