"""
分页配置
"""

from rest_framework.pagination import PageNumberPagination


class TenItemPerPagePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_number'
    max_page_size = 100