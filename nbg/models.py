from django.db import models
from django.conf import settings

class Building(models.Model):
    name = models.CharField(max_length=30)
    university = models.ForeignKey(University)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)

class App(models.Model):
    version_android = models.CharField(max_length=30)
    version_ios = models.CharField(max_length=30)

class University(models.Model):
    name = models.CharField(max_length=200)
