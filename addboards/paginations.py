from rest_framework.pagination import PageNumberPagination


class AdPagination(PageNumberPagination):
    """
    Класс для пагинации объявлений.

    Атрибуты:
        page_size (int): Количество элементов на одной странице.
    """
    page_size = 4
