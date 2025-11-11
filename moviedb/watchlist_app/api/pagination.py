from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MoviesPagination(PageNumberPagination):
    page_size = 10 # max number of records per page
    page_query_param = 'p' # controls the name for the page param
    page_size_query_param = 'size' # name of the param that controls the page size
    max_page_size = 50 # Limits the max number of records per page in case of a big number in page size param
    last_page_strings = 'end' # string that indicates the last page value for the page param


class MoviesLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50


class MoviesCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'created'