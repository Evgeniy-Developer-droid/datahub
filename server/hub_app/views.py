from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView
from hub_app.models import Phone, BountyData
from hub_app.serializers import PhoneSerializer, BountyDataSerializer
from workers_app.mixins import SecurityCodeMixin


class AddBountyDataView(CreateAPIView):
    queryset = BountyData.objects.all()
    serializer_class = BountyDataSerializer


class AddPhoneView(SecurityCodeMixin, CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
