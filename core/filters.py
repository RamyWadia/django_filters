import django_filters
from books.models import Book


class BookFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Book
        fields = {
            "name": ["istartswith"],
            "author__name": ["icontains"],
            "genre": ["exact"],
        }
