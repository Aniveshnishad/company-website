from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=200,blank=True)
    user_email=models.EmailField(max_length=200,blank=True)
    user_password=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.user_name
