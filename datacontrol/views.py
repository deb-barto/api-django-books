from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from datacontrol.models import Book, Autor
from datacontrol.serializer import BookSerializer, AutorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    @action(detail=True, methods=['get'], url_path='livros')
    def livros(self, request, pk=None):
        autor = self.get_object()
        livros = Book.objects.filter(autor=autor)
        serializer = BookSerializer(livros, many=True)
        return Response(serializer.data)