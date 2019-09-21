from django.db import models

# Create your models here.
class People(models.Model):
    FName = models.CharField(max_length=100)
    Group = models.ManyToManyField('self')
    Connections = models.CharField(max_length=1)
    
    def __str__(self):
        return self.FName