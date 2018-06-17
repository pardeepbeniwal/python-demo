from django.db import models
from datetime import datetime
from django.contrib import admin


class Book(models.Model):
    title = models.CharField(max_length=100)    
    publication_date = models.DateField()
    image = models.ImageField()

    def __str__(self):
        return self.title 
        
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')



