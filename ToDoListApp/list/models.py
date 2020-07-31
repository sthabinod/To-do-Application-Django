from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=20)
    paragraph = models.CharField(max_length=200)
    dateTime = models.DateTimeField(auto_now=True)