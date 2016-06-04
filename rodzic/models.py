from django.db import models

from django.contrib.auth.models import User
from opiekun.models import Grupa
# Create your models here.

class Dziecko(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    grupa = models.ForeignKey(Grupa)
    
    class Meta:
        verbose_name_plural = "dzieci"

    def __str__(self):
        return "{imie} {nazwisko}".format(imie=self.imie, nazwisko=self.nazwisko)
    

class Rodzic(models.Model):
    user = models.OneToOneField(User)
    dziecko = models.ForeignKey(Dziecko)
    
    class Meta:
        verbose_name_plural = "rodzice"

    def __str__(self):
        return "{imie} {nazwisko}".format(imie=self.user.first_name, nazwisko=self.user.last_name)
    
