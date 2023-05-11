from django.http.response import JsonResponse
from rest_framework.status import HTTP_403_FORBIDDEN
from django.conf import settings
import sys
sys.stdout.flush()


class SecurityCodeMixin():

    def dispatch(self, request, *args, **kwargs):
        print("____SERVER____", flush=True)
        print(request.META, flush=True)
        print(request.META.get("HTTP_SECRET_CODE", "_"), flush=True)
        print(settings.SECRET_WORKER_KEY, flush=True)
        print("____SERVER____", flush=True)
        if request.META.get("HTTP_SECRET_CODE", "_") == settings.SECRET_WORKER_KEY:
            return super().dispatch(request, *args, **kwargs)
        return JsonResponse({"error": "Access denied."}, status=403)
        
    