from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("class/", views.BookListView.as_view(), name="class_index"),
]
