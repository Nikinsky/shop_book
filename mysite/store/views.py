from .models import Author, Book
from .serializers import AuthorSerializers, BookSerializers
from rest_framework import viewsets



class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

