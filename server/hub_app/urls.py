from django.urls import path
from hub_app.views import *

urlpatterns = [
    path('phone/add', AddPhoneView.as_view()),
    path('bounty/add', AddBountyDataView.as_view()),
]

