from django.contrib import admin
from .models import ShortLink
from .mixin import BaseReadOnlyDeleteAdminMixin


class ShortLinkAdmin(BaseReadOnlyDeleteAdminMixin, admin.ModelAdmin):
    list_display =["link", "visit_number"]


admin.site.register(ShortLink, ShortLinkAdmin)
