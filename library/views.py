from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import CustomUser
from .decorators import role_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Book


# User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'library/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'library/login.html', {'form': form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Manage Books (Admins & Super Admins Only)
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def manage_books(request):
    return render(request, 'library/manage_books.html')

# Manage Users (Super Admin Only)
@login_required
@role_required(allowed_roles=['superadmin'])
def manage_users(request):
    users = CustomUser.objects.all()  # Fetch all users
    return render(request, 'library/manage_users.html', {'users': users})



# Edit User
@login_required
@role_required(allowed_roles=['superadmin'])
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.role = request.POST.get('role')
        user.save()
        messages.success(request, 'User updated successfully.')
        return redirect('manage_users')

    return render(request, 'library/edit_user.html', {'user': user})

# Delete User
@login_required
@role_required(allowed_roles=['superadmin'])
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('manage_users')

##################################################


# Manage Books (List Books)
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def manage_books(request):
    books = Book.objects.all()
    return render(request, 'library/manage_books.html', {'books': books})

# Add Book
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        published_date = request.POST.get('published_date')
        quantity = request.POST.get('quantity')

        Book.objects.create(title=title, author=author, isbn=isbn, published_date=published_date, quantity=quantity)
        messages.success(request, 'Book added successfully.')
        return redirect('manage_books')

    return render(request, 'library/add_book.html')

# Edit Book
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.isbn = request.POST.get('isbn')
        book.published_date = request.POST.get('published_date')
        book.quantity = request.POST.get('quantity')
        book.save()
        messages.success(request, 'Book updated successfully.')
        return redirect('manage_books')

    return render(request, 'library/edit_book.html', {'book': book})

# Delete Book
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully.')
    return redirect('manage_books')
