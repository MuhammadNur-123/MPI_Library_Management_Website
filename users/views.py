# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def profile_view(request):
    return render(request, 'user/profile.html', {'user': request.user})
@login_required(login_url='login')
def all_users(request):
    if not request.user.is_staff:
        return redirect('dashboard')
    users = User.objects.all()
    
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(
            Q(email__icontains=query) |
            Q(name__icontains=query) |
            Q(roll__icontains=query) |
            Q(department__icontains=query) |
            Q(membership_number__icontains=query)
        )
    else:
        users = User.objects.all()

    context = {
        'users': users,
        'search_query': query
    }
    context = {
        'users': users
    }
    return render(request, 'user/all_users.html', context)


def create_user(request):
    # if not request.user.is_staff:
    #     return redirect('all_users')
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
            return redirect('login')  # Redirect to a success page or another URL
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'user/user_registration.html')

def update_user_status(request, user_id):
    if not request.user.is_staff:
        return redirect('all_users')
    if request.method == 'POST':
        
        user = get_object_or_404(User, id=user_id)
        # Update the is_active status
        user.is_active = request.POST.get('is_active') == 'on'
        user.save()
        # Redirect back to the user list or any other appropriate page
        return redirect('all_users') 

@login_required(login_url='login')
def update_user(request, user_id):
    if not request.user.is_staff:
        return redirect('all_users')
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_users')  # Redirect to 'all_users' after updating
    else:
        form = UserForm(instance=user)
    return render(request, 'user/update_user.html', {'form': form, 'user': user})

@login_required(login_url='login')
def delete_user(request, user_id):
    if not request.user.is_staff:
        return redirect('all_users')
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('all_users')  # Redirect to 'all_users' after deletion
    return render(request, 'user/all_users.html')

