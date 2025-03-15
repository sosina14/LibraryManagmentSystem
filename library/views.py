from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import CustomUser, Book
from .forms import CustomUserCreationForm, BookForm
from .decorators import role_required

# User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('manage_books')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'library/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('manage_books')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'library/login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# Manage Books (List Books) ✅ Fixed Issue
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def manage_books(request):
    books = Book.objects.all()
    return render(request, 'library/manage_books.html', {'books': books})

# Manage Users
@login_required
@role_required(allowed_roles=['superadmin'])
def manage_users(request):
    users = CustomUser.objects.all()
    return render(request, 'library/manage_users.html', {'users': users})

# Add Book ✅ Fixed Issue
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('manage_books')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

# Edit Book
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('manage_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_book.html', {'form': form, 'book': book})

# Delete Book
@login_required
@role_required(allowed_roles=['admin', 'superadmin'])
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('manage_books')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("manage-books")  # Update with your dashboard URL
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")
