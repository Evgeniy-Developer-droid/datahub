from django.db import models


class Phone(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=500, null=True, blank=True, default="")
    city = models.CharField(max_length=500, null=True, blank=True, default="")
    meta = models.CharField(max_length=500, null=True, blank=True, default="")
    source = models.CharField(max_length=500, null=True, blank=True, default="")
