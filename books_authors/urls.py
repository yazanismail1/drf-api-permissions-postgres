from django.urls import path
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='books_list_view'),
    path('books/<int:pk>', BookDetailView.as_view(),name='books_detail_view'),
    path('authors/', AuthorListView.as_view(), name='authors_list_view'),
    path('authors/<int:pk>', AuthorDetailView.as_view(),name='authors_detail_view'),
]