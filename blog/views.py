from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.views.decorators.cache import cache_control


# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def log_in(request):
    if 'username' in request.session:
        return redirect('blog:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            login(request, user)
            return redirect('blog:home')
        else:
            messages.error(request, 'User Not Exists')
            return redirect('blog:login')

    return render(request, 'login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        return render(request, 'index.html')

    return redirect('blog:login')


def logout_user(request):
    if 'username' in request.session:
        request.session.flush()
    logout(request)
    return redirect('blog:login')


def register(request):
    form = UserCreationForm()
    print(form)
