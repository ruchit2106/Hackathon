from django.db import models

# Create your models here.

class Participant(models.Model):

    name=models.CharField(max_length=100)
    team=models.CharField(max_length=100)
    feedback_given=models.BooleanField(default=False)
    feedback=models.TextField()

class Teams(models.Model):
    TeamName=models.CharField(max_length=100)
    TeamSize=models.IntegerField(max_length=4)
    RegisterCount=models.IntegerField(max_length=4)