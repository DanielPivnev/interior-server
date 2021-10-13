from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import auth
from django.urls import reverse


# Create your views here

def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                'form': form
            }

            return render(request, 'users/login.html', context)
    else:
        context = {
            'form': UserLoginForm()
        }

        return render(request, 'users/login.html', context)


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)

        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']

            user = auth.authenticate(username=username, password=password1)
            auth.login(request, user)

            return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                'form': form
            }

            return render(request, 'users/register.html', context)
    else:
        context = {
            'form': UserRegisterForm()
        }

        return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('index'))


def profile(request):
    context = {
        'form': ''
    }

    return render(request, 'users/profile.html', context)
