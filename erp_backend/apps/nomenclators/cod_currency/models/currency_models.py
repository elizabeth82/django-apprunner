from django.db import models
from django.db.models import Model

class Currency(Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)    
    default = models.BooleanField()

    def __str__(self):
        return self.name
