from django.conf.urls import include, url
from django_project.app.views import apphome,login,signup,profile,contact,getschool

urlpatterns = [		   		   
		   url(r'^loginapp', login, name = 'loginapp'),
		   url(r'^signup', signup, name = 'signup'),
		   url(r'^profile', profile, name = 'profile'),
		   url(r'^contact', contact, name = 'contact'),
		   url(r'^getschool', getschool, name = 'getschool'),
		   url(r'^', apphome, name = 'apphome')	  
 ]
