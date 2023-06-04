from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    # create an author_name to get the author.name as it is a
    # foreign key field
    author_name = serializers.CharField(source="author.name")
    # specifying the genre to get the value not the "one letter"
    genre = serializers.CharField(source="get_genre_display")

    class Meta:
        model = Book
        fields = (
            "name",
            "author_name",
            "price",
            "genre",
        )
