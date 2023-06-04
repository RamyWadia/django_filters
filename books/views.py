from typing import Any, Dict
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import render
from core.forms import BookNameFilter
from .models import Book
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
    template_name = "books/index.html"
    context_object_name = "books"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context
