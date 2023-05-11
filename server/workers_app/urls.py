from django.urls import path
from workers_app.views import *

urlpatterns = [
    path('get', GetWorkerView.as_view())
]

