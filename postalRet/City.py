from django.db import models

class City(models.Model):
    city = models.CharField('あとで',max_length=50,blank=False)
    town = models.CharField('町',max_length=50,blank=False)
    prefecture = models.CharField('県名',max_length=5,blank=False)
    postal = models.CharField('郵便番号',max_length=10,blank=False)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return self.postal