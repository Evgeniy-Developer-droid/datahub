from django.contrib import admin
from workers_app.models import Worker


class WorkerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'status', 'created', 'updated',)

admin.site.register(Worker, WorkerAdmin)
