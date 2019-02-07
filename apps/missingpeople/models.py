from django.db import models

# Create your models here.

class People(models.Model):
    publicdate = models.CharField(max_length=999)
    name = models.CharField(max_length=999)

    def __str__(self):
        return self.name