from django.db import models

# Create your models here.

class DuyuruModel(models.Model):
    title=models.CharField(max_length=50,verbose_name="Başlık Bilgisi",null=False,blank=False)
    description=models.TextField(max_length=5000,verbose_name="İçerik Bilgisi",null=False,blank=False)

class SaatModel(models.Model):
    dersSaati=models.CharField(max_length=50,verbose_name="Ders Saati",null=False,blank=False,default="1. Ders")
    ogrenci=models.TimeField(verbose_name="Öğrenci Zili")
    ogretmen=models.TimeField(verbose_name="Öğretmen Zili")
    cikis=models.TimeField(verbose_name="Çıkış Zili")
    sesDuzeyi=models.IntegerField(verbose_name="Ses Düzeyi 0-100:",default=50)

class OgrenciMelodiModel(models.Model):
    ogrenciMelodi=models.CharField(max_length=50,verbose_name="Öğrenci Zili Melodisi:",null=False,blank=False)
    ogrenciAnons=models.BooleanField(verbose_name="Anon Kullan",default=True)
    ogrenciAnonsDers1=models.BooleanField(verbose_name="1.Ders Hariç Diğerlerinde Anons Kullan",default=False)
    ogrenciSesDuzeyi=models.IntegerField(verbose_name="Ses Düzeyi 0-100:",default=50)

class OgretmenMelodiModel(models.Model):
    ogretmenMelodi=models.CharField(max_length=50,verbose_name="Öğretmen Zili Melodisi:",null=False,blank=False)
    ogretmenAnons=models.BooleanField(verbose_name="Anon Kullan",default=True)
    ogretmenAnonsDers1=models.BooleanField(verbose_name="1.Ders Hariç Diğerlerinde Anons Kullan",default=False)
    ogretmenSesDuzeyi=models.IntegerField(verbose_name="Ses Düzeyi 0-100:",default=50)

class CikisMelodiModel(models.Model):
    cikisMelodi=models.CharField(max_length=50,verbose_name="Öğretmen Zili Melodisi:",null=False,blank=False)
    cikisSesDuzeyi=models.IntegerField(verbose_name="Ses Düzeyi 0-100:",default=50)