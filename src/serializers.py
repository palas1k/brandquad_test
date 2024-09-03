from rest_framework.serializers import ModelSerializer

from src.models import LogsInfo


class LogsSerializer(ModelSerializer):
    class Meta:
        model = LogsInfo
        exclude = ['id']
