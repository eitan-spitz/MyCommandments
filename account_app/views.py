from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account_app.forms import SignUpForm, LoginForm
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.warning(request, f"{form.cleaned_data['username']} is already in use")
                return redirect(reverse('account_app:signup'))
            user = User.objects.create_user(**form.cleaned_data)
            messages.info(request, f'{user.username} successfully created !')
            return redirect(reverse('commandments_app:commandments_filtering'))
    else:
        form = SignUpForm()

    return render(request, 'account_app/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                messages.info(request, 'Successfully logged in!')
                return redirect(reverse('commandments_app:homepage'))
            else:
                messages.error(request, 'Bad authentication....')
                return redirect(reverse('account_app:login'))

    else:
        form = LoginForm()

    return render(request, 'account_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect(reverse('account_app:login'))

@login_required
def profile(request):
    return render(request, 'account_app/profile.html')
