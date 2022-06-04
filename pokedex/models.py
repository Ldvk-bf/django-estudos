from pyexpat import model
from django.db import models

# Create your models here.


class pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("name", max_length=45)
    height = models.IntegerField("height")
    weight = models.IntegerField("weight")
    types = models.CharField("types", max_length=200)
    sprint = models.CharField("sprint", max_length=200)
