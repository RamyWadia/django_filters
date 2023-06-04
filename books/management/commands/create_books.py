from typing import Any, Optional
from django.core.management.base import BaseCommand
from books.models import Book, Author


class Command(BaseCommand):
    help = "load book data"

    def handle(self, *args: Any, **options: Any):
        # Create Authors
        orwell = Author.objects.get_or_create(name="George Orwell")[0]
        zamyatin = Author.objects.get_or_create(name="Yevgeny Zamyatin")[0]
        christie = Author.objects.get_or_create(name="Agatha Christie")[0]
        hawking = Author.objects.get_or_create(name="Stephen Hawking")[0]
        highsmith = Author.objects.get_or_create(name="Patricia Highsmith")[0]
        bradbury = Author.objects.get_or_create(name="Ray Bradbury")[0]

        # Create Books
        Book.objects.get_or_create(
            name="1984",
            author=orwell,
            price=10.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=4,
        )

        Book.objects.get_or_create(
            name="A Brief History of time",
            author=hawking,
            price=20.99,
            genre=Book.GenreChoices.NON_FICTION,
            number_in_stock=2,
        )

        Book.objects.get_or_create(
            name="We",
            author=zamyatin,
            price=16.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=12,
        )

        Book.objects.get_or_create(
            name="Death On The Nile",
            author=christie,
            price=14.99,
            genre=Book.GenreChoices.CRIME,
            number_in_stock=8,
        )

        Book.objects.get_or_create(
            name="The Price Of Salt",
            author=highsmith,
            price=9.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=9,
        )

        Book.objects.get_or_create(
            name="Fahrenheit 451",
            author=bradbury,
            price=9.99,
            genre=Book.GenreChoices.SCI_FI,
            number_in_stock=9,
        )
