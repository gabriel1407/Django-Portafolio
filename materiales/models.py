from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import URLField

# Create your models here.

class Project(models.Model):
    title = CharField(max_length=250)
    description = CharField(max_length=250)
    image = models.ImageField (upload_to = 'materiales/images/')
    url = URLField(blank=True)
