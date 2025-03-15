from django.urls import path
from .views import register, user_login, user_logout, manage_books, manage_users, edit_user, delete_user , add_book

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('manage-books/', manage_books, name='manage_books'),
    path('manage-users/', manage_users, name='manage_users'),
    path('add-book/', add_book, name='add_book'),
    path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
]

