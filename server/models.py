from django.db import models

# Create your models here.

class User(models.Model):
    user_id=models.CharField(max_length=500, primary_key=True,unique=True)
    user_name=models.CharField(max_length=150)

    def __str__(self):
        return self.user_name