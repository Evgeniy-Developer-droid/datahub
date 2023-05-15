from rest_framework import serializers
from hub_app.models import Phone, BountyData


class BountyDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = BountyData
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = '__all__'
