from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = [('male','Male'),('female','Female'),('other','Other')]
    GOAL_CHOICES = [('lose','Lose Weight'),('gain','Gain Weight'),('maintain','Maintain Weight')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    weight = models.FloatField(null=True, blank=True)  # kg
    height = models.FloatField(null=True, blank=True)  # cm
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES, default='maintain')

    def __str__(self):
        return f"{self.user.username} Profile"
from django.contrib.auth.models import User
