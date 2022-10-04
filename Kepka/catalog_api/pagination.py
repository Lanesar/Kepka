from rest_framework.pagination import PageNumberPagination



class BestsellersPagination(PageNumberPagination):

    page_size = 6
    page_query_param = 'page'


class StockPagination(PageNumberPagination):

    page_size = 6
    page_query_param = 'page'


class PaginateProduct(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 12
    max_page_size = 10000



