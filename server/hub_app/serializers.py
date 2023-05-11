from rest_framework import serializers
from hub_app.models import Phone


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = '__all__'
