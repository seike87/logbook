from django.db import models
from django.utils import timezone
# Create your models here.

class Logs(models.Model):
    datum = models.DateTimeField(default=timezone.now)
    name = models.CharField('Name', max_length=100)
    vorname = models.CharField('Vorname', max_length=100)
    ziel = models.CharField('Ziel', max_length=500)
    grund = models.CharField('Grund', max_length=200)
    von = models.TimeField('Von')
    bis = models.TimeField('Bis')
    kostenstelle = models.CharField('Kostenstelle', max_length=12)
    projekt = models.CharField('Projekt', max_length=200)



    def __str__(self):
        return self.grund
