from django.contrib import admin
from .models import  Book,UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Book)
