from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    

class question(models.Model):

    CATEGORY_CHOICES = (
        ('ECO','Conference'),
        ('HIS','Workshops & Training'),
        ('BAK','College Fest'),
        ('GOV','Sports Event'),
        ('PSY','Entertainment Events'),
    )
    ANSWER_CHOICES = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    answer = models.CharField(max_length=1,choices=ANSWER_CHOICES)
    category = models.CharField(max_length=3,choices=CATEGORY_CHOICES)
    userAtt = models.ForeignKey(user,default=None,on_delete=models.CASCADE)
    level = models.IntegerField(default=0)


    def __str__(self):
        return self.text
