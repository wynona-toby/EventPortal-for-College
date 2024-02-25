from django.db import models
#create your model here
class Student(models.Model):
  name = models.CharField(max_length=100, null=True)
  rollno = models.CharField(max_length=100, primary_key=True)
  email = models.CharField(max_length=100, null=True)
  club = models.CharField(max_length=100, null=True)
  
  def __str__(self):
    return self.name


class Faculty(models.Model):
  name = models.CharField(max_length=100, null=True)
  id = models.CharField(max_length=100, primary_key=True)
  email = models.CharField(max_length=100, null=True)
  headof = models.CharField(max_length=100, null=True)
  HOD =  models.CharField(max_length=1, null=True)
  
  def __str__(self):
    return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    days = models.CharField(max_length=2)
    location = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    club = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    intake = models.IntegerField()
    highlight_event = models.TextField()
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
