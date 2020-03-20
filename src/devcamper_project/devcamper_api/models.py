from django.db import models
from django.contrib.auth.models import User


class Users(User):
    def __str__(self):
        return self.username

class Courses(models.Model):  
    
    title = models.CharField(max_length = 50, unique=True)
    description = models.CharField(max_length=500)
    weeks = models.PositiveIntegerField()
    tuition = models.PositiveIntegerField()
    minimumSkill = models.CharField(max_length=15)
    scholarhipsAvailable = models.BooleanField()
    
    def __str__(self):
        return self.title    
   
    
    
class Bootcamps(models.Model):
    
    publisher = models.OneToOneField(Users,on_delete=models.CASCADE)
    courses = models.ManyToManyField(Courses)
    name = models.CharField(unique = True, max_length = 50)
    address = models.TextField()
    zipcode = models.CharField(max_length = 6,blank=True)
    website = models.URLField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    description = models.CharField(max_length = 500)
    careers = models.CharField(max_length = 50)
    housing = models.BooleanField()
    jobAssistance = models.BooleanField()
    jobGuarantee = models.BooleanField()
    acceptGi = models.BooleanField()
    
    def __str__(self):
        return self.name


class Reviews(models.Model):  
    
    forWhichBootcamp = models.ForeignKey(Bootcamps,models.CASCADE)
    title = models.CharField(max_length = 50, unique=True)
    text = models.CharField(max_length=500)
    rating = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title 