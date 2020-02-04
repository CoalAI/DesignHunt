"""
RestInterface.admin
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from authentication.models import User
from promotions.models import MailGun

admin.site.site_header = _('Design Hunt')
admin.site.site_title = _('Design Hunt')


class CustomUserAdmin(UserAdmin):
    """
    To added extra fields and prieous fields togather
    """
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('contact_number',)}),
    )


admin.site.register(MailGun)
admin.site.register(User, CustomUserAdmin)
