from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView
from workers_app.mixins import SecurityCodeMixin
from workers_app.models import Worker
from workers_app.serializers import WorkerSerializer


class GetWorkerView(SecurityCodeMixin, GenericAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get(self, request):
        instance = Worker.objects.filter(name=request.GET.get("name", "_"))
        if instance.exists():
            instance = instance.first()
            serializer = WorkerSerializer(instance)
            return Response(serializer.data)
        return Response({"error": "Not found"})
