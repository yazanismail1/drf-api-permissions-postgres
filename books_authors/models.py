from django.db import models
from django.contrib.auth import get_user_model

class Book(models.Model):
    book = models.CharField(max_length=255)
    description = models.TextField()
    isbn13 = models.BigIntegerField(help_text="Enter a 13 digit number with no spaces and/or dashes", default=0000000000000)
    author = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.book

class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dob = models.DateField(help_text="Enter the DOB in this format YYY-MM-DD", auto_now=False)
    nationality = models.CharField(max_length=255)
    number_of_publishes = models.IntegerField(help_text="Enter a number with no spaces and/or dashes", default=0)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.name
