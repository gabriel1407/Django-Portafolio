from django.db import models
import datetime


class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    data = models.DateField(datetime.date.today)
