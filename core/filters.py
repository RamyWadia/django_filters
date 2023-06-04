import django_filters
from books.models import Book
from django import forms


class BookFilter(django_filters.FilterSet):
    # override the price field to make it rangeFilter
    price = django_filters.RangeFilter()
    # override the genre field to use multiple choice values
    genre = django_filters.MultipleChoiceFilter(
        choices=Book.GenreChoices.choices,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Book
        fields = {
            "name": ["icontains"],
            "author__name": ["istartswith"],
        }
