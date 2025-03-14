from django.urls import path
from .views import register, user_login, user_logout

from .views import manage_books, manage_users, edit_user, delete_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('manage-books/', manage_books, name='manage_books'),
    path('manage-users/', manage_users, name='manage_users'),
    path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
]

