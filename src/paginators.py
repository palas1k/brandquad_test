from rest_framework.pagination import PageNumberPagination


class LogsPaginator(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = 10
