from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Manager(models.Model):
    manager_name=models.CharField(max_length=200,blank=True)
    manager_password=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.manager_name