from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView
from hub_app.models import Phone
from hub_app.serializers import PhoneSerializer
from workers_app.mixins import SecurityCodeMixin


class AddPhoneView(SecurityCodeMixin, CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
