from django.contrib import admin
from hub_app.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    search_fields = ('number',)
    list_display = ('number', 'name', 'city', 'meta', 'source', 'created',)

admin.site.register(Phone, PhoneAdmin)
