from django.db import models

# Create your models here.

class DuyuruModel(models.Model):
    title=models.CharField(max_length=50,verbose_name="Başlık Bilgisi",null=False,blank=False)
    description=models.TextField(max_length=500,verbose_name="İçerik Bilgisi",null=False,blank=False)
