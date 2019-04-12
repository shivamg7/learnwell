from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class user(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    profession = models.CharField(max_length=30)


    def __str__(self):
        return self.username

class Question(models.Model):

    CATEGORY_CHOICES = (
        ('ECO','Economics'),
        ('HIS','History'),
        ('BAK','Banking'),
        ('GOV','Government'),
        ('PSY','Psycology'),
    )
    ANSWER_CHOICES = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    optionA = models.CharField(max_length=300)
    optionB = models.CharField(max_length=300)
    optionC = models.CharField(max_length=300)
    optionD = models.CharField(max_length=300)
    answer = models.CharField(max_length=1,choices=ANSWER_CHOICES)
    category = models.CharField(max_length=3,choices=CATEGORY_CHOICES)
    level = models.IntegerField(default=5)


    def __str__(self):
        return self.text
