
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hub/', include('hub_app.urls')),
    path('workers/', include('workers_app.urls')),
]
