from django.db import models
from datetime import datetime

class User(models.Model):
	firstname = models.CharField(max_length = 50)
	lastname = models.CharField(max_length = 50)
	pwdhash = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50,unique=True)  
	status = models.IntegerField(default='0', editable=False)  
	created = models.DateTimeField(auto_now=True)	
	

	class Meta:
		managed = False
		db_table = "users"
