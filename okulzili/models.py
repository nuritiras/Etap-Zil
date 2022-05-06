from trace import Trace
from django.db import models

# Create your models here.

class okulzili(models.Model):

    name = models.TimeField(verbose_name='Toplanma Saati')
    description = models.TimeField(verbose_name='Eklenme Saati')
    isPublished = models.BooleanField(default=True)
