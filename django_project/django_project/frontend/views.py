from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django_project.frontend.forms import SignUpForm, LoginForm,ProfileForm
from django_project.frontend.models import User
from datetime import datetime
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


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
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                if form.checkPassword(form.cleaned_data['pwdhash'],user.pwdhash):
                    request.session['user_id'] = str(user.id)
                    return redirect('profile')
                else :
                   messages.error(request, 'password did not match')
                   return redirect('login')
            except ObjectDoesNotExist:
                messages.error(request, 'Email/password did not match')
                return redirect('login')

        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def profile(request):
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id)[0]
        form = ProfileForm(request.POST or None, initial=model_to_dict(user))
        if form.is_valid():
            form = ProfileForm(request.POST, instance=user)
            j = form.save(commit=False)
            j.save()
            messages.success(request, 'Your profile has been updated successfully')
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect("login")
