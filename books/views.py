from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import ListView
from django.shortcuts import render
from .models import Book
from core.serializers import BookSerializer
from core.filters import BookFilter


def index(request):
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())

    context = {
        "form": book_filter.form,
        "books": book_filter.qs,
    }
    return render(request, "books/index.html", context)


class BookListView(ListView):
    queryset = Book.objects.all()
    # the next line filtering may come handy and could also be used in function based view.
    # queryset = Book.objects.filter(number_in_stock__gt=0)
    template_name = "books/index.html"
    context_object_name = "books"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
