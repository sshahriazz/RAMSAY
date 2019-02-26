from .forms import RegistrationForm, UserUpdateForm, UserPassChangeForm, UserPhotoUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def user_login_view(request):
    # Creating user object & authenticating.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # checking if user is valid
        if user is not None:
            login(request, user)
            messages.success(request, f'{user.username} is logged in successfully')
            return redirect('landing_page')  # on successful login redirect to home
        else:
            messages.info(request, f'Invalid Username or Password.')
            return redirect('accounts:login')  # on failure redirect to login itself
    else:
        return render(request, 'accounts/login.html', {})


def user_logout_view(request):
    logout(request)
    messages.warning(request, f'You have been logged out. Login Again.')
    return redirect('accounts:login')


@login_required(redirect_field_name='login', login_url='accounts:login')
def user_profile_view(request):
    if User.is_authenticated:
        return render(request, 'accounts/profile.html', {})
    else:
        messages.warning(request, f'You are not logged in please login first.')


def user_register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username, password=password1)
            login(request, user)
            messages.success(request, f'{user.username} Registered successfully.')
            return redirect('landing_page')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form_info = UserUpdateForm(request.POST, instance=request.user)
        form_img = UserPhotoUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form_info.is_valid() and form_img.is_valid():
            form_info.save()
            form_img.save()
            messages.success(request, f'Profile updated successfully.')
            return redirect('accounts:profile')
    else:
        form_info = UserUpdateForm(instance=request.user)
        form_img = UserPhotoUpdateForm(instance=request.user.profile)

    context = {
        'form_info': form_info,
        'form_img': form_img,
    }
    return render(request, 'accounts/update_profile.html', context)


def change_password_view(request):
    if request.method == 'POST':
        form = UserPassChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, f'Password Updated.')
            return redirect('accounts:profile')
    else:
        form = UserPassChangeForm(user=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
