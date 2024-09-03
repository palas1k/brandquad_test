from rest_framework import status
from rest_framework.test import APITestCase

from src.models import LogsInfo


class LogsApiTestCase(APITestCase):
    def setUp(self):
        self.credentials = {
            "ip_address": "127.0.0.1",
            "date_time": "2020-02-02T00:00:00",
            "http_method": "GET",
            "uri": "/api/v1/logs",
            "response_code": "200",
            "response_size": 5,
        }
        self.log_info = LogsInfo.objects.create(**self.credentials)

    def test_get_logs(self):
        response = self.client.get(f"/api/v1/logs")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.credentials)