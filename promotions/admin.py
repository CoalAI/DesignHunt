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


class MailGunAdmin(admin.ModelAdmin):
    list_display = ('sender', 'subject',)
    search_fields = ('sender', 'subject', 'body_plain', 'body_html',)


admin.site.register(MailGun, MailGunAdmin)
admin.site.register(User, CustomUserAdmin)
