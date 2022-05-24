from django.db import models
from django.contrib.auth.models import User
# Create your models here.
POSITION_CHOICES = (
    ('software engineer','SOFTWARE ENGINEER'),
    ('web developer', 'WEB DEVELOPER'),
    ('technical engineer','TECHNICAL ENGINEER'),
    ('data scientist','DATA SCIENTIST'),
)
# class Position(models.Model):
#     title= models.CharField(max_length=100)

class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    position= models.CharField(max_length=100, choices=POSITION_CHOICES, default='software engineer')

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     forget_password_token =models.CharField(max_length=100)
#     created_at= models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username