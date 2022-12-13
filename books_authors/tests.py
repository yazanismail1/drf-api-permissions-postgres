from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
from django.contrib.auth import get_user_model
from .models import Book, Author

from django.urls import reverse

class ThingTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_book= Book.objects.create(
            book="book1",
            description="desc1",
            isbn13=1234,
            author="test1",
            owner=testuser1,
        )
        test_book.save()

        test_author= Author.objects.create(
            name="Yazan",
            description="desc1",
            dob='1998-04-03',
            nationality='Jordan',
            number_of_publishes=0,
            owner=testuser1,
        )
        test_author.save()

    def setUp(self):
        self.client.login(username='testuser1', password="pass")

    def test_books_model(self):
        thing = Book.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_book = str(thing.book)
        actual_description = str(thing.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_book, "book1")
        self.assertEqual(
            actual_description, "desc1"
        )

    def test_authors_model(self):
        author = Author.objects.get(id=1)
        actual_owner = str(author.owner)
        actual_dob = str(author.dob)
        actual_number_of_publishes = str(author.number_of_publishes)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_dob, "1998-04-03")
        self.assertEqual(
            actual_number_of_publishes, '0'
        )

    def test_get_books_list(self):
        url = reverse("books_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data
        self.assertEqual(len(books), 1)

    def test_get_authors_list1(self):
        url = reverse("authors_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        authors = response.data
        self.assertEqual(len(authors), 1)
        
    def test_auth_required(self):
        self.client.logout()
        url = reverse("books_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_required1(self):
        self.client.logout()
        url = reverse("authors_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("books_detail_view", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete1(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("authors_detail_view", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
