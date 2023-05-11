from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from django.conf import settings

class SecurityCodeMixin():

    def dispatch(self, request, *args, **kwargs):
        if request.META.get("SECRET_CODE", "_") != settings.SECRET_WORKER_KEY:
            return Response({"error": "Access denied."}, status=HTTP_403_FORBIDDEN)
        return super().dispatch(request, *args, **kwargs)
    