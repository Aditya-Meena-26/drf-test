from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorListCreateView(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetailsView(APIView):
    def get(self, request, id, format=None):
        author = Author.objects.get(id=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

class BookListCreateView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailsView(APIView):
    def get(self, request, id, format=None):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
