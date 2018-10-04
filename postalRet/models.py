from django.db import models


class Place(models.Model):
    city = models.CharField(max_length=50, blank=False)
    town = models.CharField(max_length=50, blank=False)
    prefecture = models.CharField(max_length=5, blank=False)
    postal = models.CharField(max_length=10, blank=False)
    x = models.FloatField()
    y = models.FloatField()
