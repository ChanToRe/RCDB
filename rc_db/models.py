from django.db import models
from django.db.models.base import Model

# Create your models here.
class rc_db(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject