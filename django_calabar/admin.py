from django.contrib import admin
from django_calabar.models import TunnelConfig, CalabarConfig

class TunnelConfigAdmin(admin.ModelAdmin):
    pass

admin.site.register(TunnelConfig, TunnelConfigAdmin)


class CalabarConfigAdmin(admin.ModelAdmin):
    pass

admin.site.register(CalabarConfig, CalabarConfigAdmin)