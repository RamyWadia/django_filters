import django_filters
from books.models import Book


class BookFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Book
        fields = {
            "name": ["icontains"],
            "author__name": ["istartswith"],
            "genre": ["exact"],
        }
