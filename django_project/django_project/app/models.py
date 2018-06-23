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

class State(models.Model):
	name = models.CharField(max_length = 50)	
	class Meta:
		managed = False
		db_table = "state"
		
class City(models.Model):
	name = models.CharField(max_length = 50)
	state = models.ForeignKey(State, on_delete=models.CASCADE)
	
	class Meta:
		managed = False
		db_table = "city"
		
class Location(models.Model):
	name = models.CharField(max_length = 50)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	
	class Meta:
		managed = False
		db_table = "location"
		
	def __str__(self):
		return self.name
			
class School(models.Model):
	school_name = models.CharField(max_length = 50)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.school_name


	def getSchool(models,arg):
		#return models.objects.all()
		#return models.objects.get(pk=2)
		#return models.objects.get(school_name = arg)
		queryset =  models.objects.all().filter(location__city__state=4).select_related() 
		
		print(queryset.query)
		return queryset
		

	class Meta:
		managed = False
		db_table = "school"


	
