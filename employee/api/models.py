from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    salary_amount = models.PositiveIntegerField()
    promotion_points = models.IntegerField()

    def __str__(self):
        return self.first_name
    
