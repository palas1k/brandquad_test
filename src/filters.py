from django_filters import FilterSet, DateFromToRangeFilter, CharFilter

from src.models import LogsInfo


class LogsFilterset(FilterSet):
    date_time_filter = DateFromToRangeFilter()
    response_code_search = CharFilter(field_name='response_code', lookup_expr='icontains')

    class Meta:
        model = LogsInfo
        fields = ['date_time_filter', 'response_code_search']
