from rest_framework import viewsets
from books.api.serializers import BookSerializer
from books.models import Books


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
