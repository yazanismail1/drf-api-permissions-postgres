from rest_framework import serializers
from .models import Book, Author
from django.contrib.auth import get_user_model
from django.db import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields=('id','book', 'description', 'isbn13', 'author', 'owner')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields=['id','name', 'description', 'dob', 'nationality', 'number_of_publishes', 'owner']
