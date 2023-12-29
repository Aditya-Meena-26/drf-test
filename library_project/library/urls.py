# library/urls.py
from django.urls import path
from .views import AuthorListCreateView, AuthorDetailsView, BookListCreateView, BookDetailsView

urlpatterns = [
    path('api/authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/authors/<int:id>/', AuthorDetailsView.as_view(), name='author-details'),
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:id>/', BookDetailsView.as_view(), name='book-details'),
]
