from django.db import models

# Create your models here.

class user(models.Model):
    First_Name =models.CharField(max_length=200)
    Last_Name =models.CharField(max_length=200)
    Email_id = models.EmailField(max_length=254, unique=True)
    def __str__(self):
        return self.First_Name
