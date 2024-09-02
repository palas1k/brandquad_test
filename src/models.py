from django.db import models


# Create your models here.
class LogsInfo(models.Model):
    ip_address = models.TextField()
    data = models.TextField()
    http_method = models.TextField()
    uri = models.TextField()
    response_code = models.TextField()
    response_size = models.TextField()