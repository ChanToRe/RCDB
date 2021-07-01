from django.db import models
from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
from django.db.models.fields import TextField
from django.db.models.fields.reverse_related import ManyToOneRel

# Create your models here.
class rcdb(models.Model):
    Name = models.CharField(max_length=11)
    State = models.CharField(max_length=15)
    City = models.CharField(max_length=15)
    Site = models.CharField(max_length=15)
    Material = models.CharField(max_length=15)
    Weight_g = models.FloatField()
    Laboratory = models.CharField(max_length=15)
    LabID = models.CharField(max_length=15)
    Age_BP = models.IntegerField()
    Error = models.IntegerField()
    Report = models.TextField()