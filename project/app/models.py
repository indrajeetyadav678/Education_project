from django.db import models

# Create your models here.

class Registration(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.CharField(max_length=30)
    Con_password=models.CharField(max_length=30)

    def __str__(self):
        return self.Email