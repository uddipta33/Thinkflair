from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import Author, Book
from .serializers import AuthorSerializer,BookSerializer

# Create your views here.

class AuthorList(APIView):
    # used to get all the objects of Author Model
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data)
    
    #used to create an object of Author model
    def post(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class AuthorDetail(APIView):
    # used to fetch a specific object of Author Model
    def get(self, request, pk):
        try:
            author = Author.objects.get(id=pk)
        except Author.DoesNotExist:
            raise Http404
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data)

class BookList(APIView):
    #used to get all the objects of Book Model
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
    # used to create an object of Book Model
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookDetail(APIView):
    # used to fetch a specific object of Book Model
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)


        

