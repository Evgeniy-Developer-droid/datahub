from django.http.response import JsonResponse
from rest_framework.status import HTTP_403_FORBIDDEN
from django.conf import settings

class SecurityCodeMixin():

    def dispatch(self, request, *args, **kwargs):
        if request.META.get("SECRET_CODE", "_") == settings.SECRET_WORKER_KEY:
            return super().dispatch(request, *args, **kwargs)
        return JsonResponse({"error": "Access denied."}, status=403)
        
    