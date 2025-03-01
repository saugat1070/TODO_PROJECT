from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10,null=False,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
