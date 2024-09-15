from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from books.models import Book, Author
from users.models import User
from library.models import Loan



# def custom_login(request):
#     # Custom login logic
#     return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user based on email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Redirect to the dashboard or home page
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        department = request.POST.get('department')
        session = request.POST.get('session')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        membership_number = request.POST.get('membership_number')
        user_type = request.POST.get('user_type')
        image = request.FILES.get('image')
        password = request.POST.get('password')

        # Check if the required fields are provided
        if email and user_type:
            user = User(
                email=email,
                name=name,
                roll=roll,
                department=department,
                session=session,
                phone_number=phone_number,
                address=address,
                membership_number=membership_number,
                user_type=user_type,
                image=image,
            )
            user.set_password(password)
            user.save()
            messages.success(request, 'User created successfully.')
            return redirect('login/login')  # Redirect to a success page or another URL
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'login/registration.html')

def forgot_password_view(request):
    return render(request, 'login/forgotpassword.html')


@login_required(login_url='login')
def dashboard_view(request):
    total_members = User.objects.filter(user_type='MEM').count()
    total_books = Book.objects.count()
    total_authors = Author.objects.count()
    total_orders = Loan.objects.count()  # Assuming "Order" is represented by Loan
    total_admin_librarians = User.objects.filter(user_type__in=['ADM', 'LIB']).count()

    context = {
        'total_members': total_members,
        'total_books': total_books,
        'total_authors': total_authors,
        'total_orders': total_orders,
        'total_admin_librarians': total_admin_librarians,
    }

    return render(request, 'admin/dashboard.html', context)