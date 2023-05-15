from django.contrib import admin
from hub_app.models import Phone, BountyData


class BountyDataAdmin(admin.ModelAdmin):
    search_fields = ('source',)
    list_display = ('source', 'data', 'created',)

admin.site.register(BountyData, BountyDataAdmin)


class PhoneAdmin(admin.ModelAdmin):
    search_fields = ('number',)
    list_display = ('number', 'name', 'city', 'meta', 'source', 'created',)

admin.site.register(Phone, PhoneAdmin)
