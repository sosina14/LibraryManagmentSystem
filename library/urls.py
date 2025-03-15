from django.urls import path
from .views import register, user_login, user_logout, manage_books, manage_users, add_book, edit_book, delete_book

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('manage-books/', manage_books, name='manage_books'),
    path('manage-users/', manage_users, name='manage_users'),
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
]

