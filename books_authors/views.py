from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers  import BookSerializer, AuthorSerializer
from .models import Book, Author
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class BookListView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    permission_classes=[IsOwnerOrReadOnly, IsAuthenticated]

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    permission_classes=[IsOwnerOrReadOnly, IsAuthenticated]

class AuthorListView(ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class= AuthorSerializer
    permission_classes=[IsOwnerOrReadOnly, IsAuthenticated]

class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class= AuthorSerializer
    permission_classes=[IsOwnerOrReadOnly, IsAuthenticated]