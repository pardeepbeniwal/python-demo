from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password,check_password

#from django.contrib.auth.models import User
from django_project.app.models import User


class SignUpForm(ModelForm):
    firstname = forms.CharField(max_length=30, required=True,error_messages={'required': 'Please enter your first name'})
    lastname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='')
    pwdhash = forms.CharField(widget=forms.PasswordInput(),label='Password',max_length=254, help_text='',error_messages={'required': 'Please enter your password'})



    def createPassword(self,pwdhash):
        return make_password(password=pwdhash,salt=None,hasher='pbkdf2_wrapped_sha1' )

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email')

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True,help_text='')
    pwdhash = forms.CharField(widget=forms.PasswordInput(),label='Password',max_length=254, help_text='',error_messages={'required': 'Please enter your password'})

    def checkPassword(self, pwdtxt,pwdhash):
        return check_password(pwdtxt,pwdhash)

class ProfileForm(ModelForm):
    firstname = forms.CharField(max_length=30, required=True,error_messages={'required': 'Please enter your first name'})
    lastname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('firstname', 'lastname')
