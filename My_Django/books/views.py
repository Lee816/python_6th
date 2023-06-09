from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Book, Author, Publisher

# Create your views here.


class BooksModelView(TemplateView):
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_list"] = ["Book", "Author", "Publisher"]
        return context


class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


class BookDetailView(DetailView):
    model = Book


class AuthorDetailView(DetailView):
    model = Author


class PublisherDetailView(DetailView):
    model = Publisher
