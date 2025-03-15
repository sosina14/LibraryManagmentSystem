from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Book, User
from .forms import BookForm, UserRegistrationForm

# User registration view
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

# User login view
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("manage_books")
    return render(request, "login.html")

# User logout view
def user_logout(request):
    logout(request)
    return redirect("login")

# Manage books view (Added this function)
@login_required
def manage_books(request):
    books = Book.objects.all()
    return render(request, "manage_books.html", {"books": books})

# Manage users view
@login_required
def manage_users(request):
    users = User.objects.all()
    return render(request, "manage_users.html", {"users": users})

# Edit user view
@login_required
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("manage_users")
    else:
        form = UserRegistrationForm(instance=user)
    return render(request, "edit_user.html", {"form": form})

# Delete user view
@login_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("manage_users")
    return render(request, "confirm_delete.html", {"user": user})

# Add book view
@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_books")
    else:
        form = BookForm()
    return render(request, "add_book.html", {"form": form})
