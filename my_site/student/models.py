from django.db import models

# Create your models here.
#Create a class for the student model
class Student(models.Model):
    #Create a field for the student's name
    name = models.CharField(max_length=50)
    #Create a field for the student's age
    age = models.IntegerField()
    #Create a field for the student's email
    email = models.EmailField()