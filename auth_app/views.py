from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, CustomUserCreationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

def dashboard_view(request):
    user = request.user
    return render(request, 'dashboard.html', {'user': user})

def logout_view(request):
    
    return redirect('login')
@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            request.user.username = form.cleaned_data['name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect('dashboard')
    else:
        initial_data = {'name': request.user.username, 'email': request.user.email}
        form = ProfileEditForm(initial=initial_data)
    return render(request, 'profile_edit.html', {'form': form})

def check_email_existence(request):
    if request.method == 'POST' and request.is_ajax():
        email = request.POST.get('email')
        # Implement your own logic to check email existence
        email_exists = False  # Placeholder for checking email existence
        return JsonResponse({'exists': email_exists})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
@login_required
@never_cache
def protected_view(request):
     return render(request, 'login.html')