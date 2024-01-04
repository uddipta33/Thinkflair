from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
    path('authors/<str:pk>/', views.AuthorDetail.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<str:pk>/', views.BookDetail.as_view()),
]