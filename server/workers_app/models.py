from django.db import models


class Worker(models.Model):
    STATUS = (
        ("work", "Work", ),
        ("stop", "Stop", ),
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50, choices=STATUS, default="stop")
    params = models.TextField(blank=True, default="", help_text="Send params with space delimeter")
