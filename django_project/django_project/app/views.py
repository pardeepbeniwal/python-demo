from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django_project.app.forms import SignUpForm, LoginForm,ProfileForm
from django_project.app.models import User,School
from datetime import datetime
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def getschool(request):	
	arg = 'hisar-school'
	data = School.getSchool(School,arg)
	print(44444444)
	print(data)
	#data = data.school_name
	print(3333)
	#now = datetime.now()-timedelta(433)
	#html = "<html><body>It is now %s</body></html>"%now.date()
	#return HttpResponse(html)
	return render(request, "home.html", {'data':data})
	
def apphome(request):
    text = "This is APP HOME "
    return redirect("http://stackoverflow.com/")
    return render(request, "home.html", {})

def contact(request):
    text = "contact page here "
    return render(request, "contact.html", {})

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
