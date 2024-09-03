from django.db import models


# Create your models here.
class LogsInfo(models.Model):
    ip_address = models.TextField(null=True)
    date_time = models.DateTimeField(null=True)
    http_method = models.TextField(null=True)
    uri = models.TextField(null=True)
    response_code = models.TextField(null=True)
    response_size = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "LogsInfo"

    def __str__(self):
        return str(self.date_time)

