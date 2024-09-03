from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from services.saver import LogsSaver
from src.filters import LogsFilterset
from src.models import LogsInfo
from src.paginators import LogsPaginator
from src.serializers import LogsSerializer


# Create your views here.
class LogsViewSet(ModelViewSet):
    queryset = LogsInfo.objects.all()
    serializer_class = LogsSerializer
    pagination_class = LogsPaginator
    filterset_class = LogsFilterset
    http_method_names = ["get", "post"]

    def get(self, request):
        return Response(self.get_serializer(LogsInfo.objects.all()).data)

    def create(self, request):
        # сохранение в базе данных из файла или ссылки
        LogsSaver().save_logs_in_db()
        return Response(self.get_serializer(LogsInfo.objects.all()).data)
