from django.db import models

# Create your models here.

class Person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=12)
    email=models.EmailField()
    date_of_birth=models.DateField()
 
    def _str__(self):
        return self.first_name +" "+self.last_name
    
