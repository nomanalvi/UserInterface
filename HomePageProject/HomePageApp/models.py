from django.db import models

# Create your models here.
class Allcourses(models.Model):
    coursename = models.CharField(max_length=200)
    coursecode = models.CharField(max_length=200)
    insname = models.CharField(max_length=200)

class details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete=models.CASCADE)
