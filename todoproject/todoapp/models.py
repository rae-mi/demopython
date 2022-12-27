
from django.db import models


# Create your models here.

class Lists(models.Model):
    name = models.CharField(max_length=250)
    order = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name


