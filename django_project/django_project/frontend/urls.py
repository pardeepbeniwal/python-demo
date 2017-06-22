from django.conf.urls import include, url
from django_project.frontend.views import home,login,signup,profile

urlpatterns = [		   		   
		   url(r'^user/login', login, name = 'login'),
		   url(r'^user/signup', signup, name = 'signup'),
		   url(r'^user/profile', profile, name = 'profile'),
		   #url(r'^user/profile/(\d+)', profile, name = 'profile'),
		   url(r'^', home, name = 'home'),
 ]
