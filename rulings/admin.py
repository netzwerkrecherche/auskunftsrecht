from django.contrib import admin

from .models import Ruling


class RulingAdmin(admin.ModelAdmin):
    list_display = ('file_reference', 'court', 'jurisdiction',)
    list_filter = ('jurisdiction', 'court',)
    search_fields = ['file_reference']

admin.site.register(Ruling, RulingAdmin)
