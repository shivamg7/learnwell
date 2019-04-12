from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class user(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    profession = models.CharField(max_length=30)
    rating = models.IntegerField(default=1500)


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
    level = models.IntegerField(default=2)
    explanation = models.CharField(max_length=500,default="Lorem")
    rating = models.IntegerField(default=500)
    counter = models.IntegerField(default=0)
    ratingChange = models.IntegerField(default=0)


    def __str__(self):
        return self.text

class Attempt(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    userAtt = models.ForeignKey(user,on_delete=models.CASCADE)
    result = models.CharField(max_length=1,choices=(('C','Correct'),('W','Wrong')))
    confidenceLevel = models.IntegerField()

class Stats(models.Model):
    userV = models.ForeignKey(user,on_delete=models.CASCADE)
    quizid = models.IntegerField()
    preSkill = models.IntegerField()
    postSkill = models.IntegerField()
    score = models.IntegerField()
    confidenceLevel = models.IntegerField()
