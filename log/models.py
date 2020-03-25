from django.db import models
from django.utils import timezone
# Create your models here.

class Logs(models.Model):
    datum = models.DateTimeField(default=timezone.now)
    name = models.CharField('Name', max_length=100)
    vorname = models.CharField('Vorname', max_length=100)
    ziel = models.TextField('Ziel')
    grund = models.CharField('Grund', max_length=200)
    von = models.DateField('Von')
    bis = models.DateField('Bis')
    kostenstelle = models.CharField('Kostenstelle', max_length=50)
    projekt = models.CharField('Projekt', max_length=200)

    def __str__(self):
        return self.title
