from django.conf.urls import include, url
from django_project.frontend.views import home,login,signup,profile,contact

urlpatterns = [		   		   
		   url(r'^login', login, name = 'login'),
		   url(r'^signup', signup, name = 'signup'),
		   url(r'^profile', profile, name = 'profile'),
		   url(r'^contact', contact, name = 'contact'),
		   #url(r'^user/profile/(\d+)', profile, name = 'profile'),
		   url(r'^', home, name = 'home'),
 ]
