from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_project.frontend.forms import SignUpForm, LoginForm
from django_project.frontend.models import User
from datetime import datetime


def home(request):
    text = "Displaying article Numberasd "
    return render(request, "home.html", {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.pwdhash = form.createPassword(form.cleaned_data['pwdhash'])
            user.save()
            request.session['user_id'] = str(user.id)
            return redirect('profile')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})


def login(request):
    # num_results = User.objects.filter(email=cleaned_info['username']).count()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(444444444)
            user = User.objects.filter(email=form.cleaned_data['email'])
            print(user)
            user.pwdhash = form.createPassword(form.cleaned_data['pwdhash'])
            user.save()
            request.session['user_id'] = str(user.id)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def profile(request):
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        return render(request, "profile.html", {'user_id': user_id})
    else:
        return redirect("login")
