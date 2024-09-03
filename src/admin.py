from django.contrib import admin

from src.models import LogsInfo


# Register your models here.
@admin.register(LogsInfo)
class LogsInfoAdmin(admin.ModelAdmin):
    list_display = (
        "ip_address",
        "date_time",
        "http_method",
        "uri",
        "response_code",
        "response_size",
    )
    list_display_links = (
        "ip_address",
        "date_time",
        "http_method",
        "uri",
        "response_code",
        "response_size",)
    search_fields = (
        "ip_address",
        "date_time",
        "http_method",
        "uri",
        "response_code",
        "response_size",)
