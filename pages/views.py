from multiprocessing import context
import multiprocessing
from django.shortcuts import render
from django.http import HttpResponse
from okulzili.models import DuyuruModel,SaatModel,OgrenciMelodiModel,OgretmenMelodiModel,CikisMelodiModel
from gtts import gTTS
from pygame import mixer
from django.contrib import messages

mixer.init()

def index(request):
    okulzilis = DuyuruModel.objects.all()

# Create your views here.
# http://127.0.0.1:8000/

def index(request):
    return render(request,'pages/index.html')

def hemencal(request):
    return render(request,'pages/hemencal.html')

def saatler(request):
    if request.method == 'POST':
        sesseviyesi=request.POST['sesseviyesi']
        # Tören:
        zaman0745 = request.POST['zaman0745']
        zaman0756 = request.POST['zaman0756']
        zaman0759 = request.POST['zaman0759']
        # 1. Ders:
        zaman0757 = request.POST['zaman0757']
        zaman0800 = request.POST['zaman0800']
        zaman0840 = request.POST['zaman0840']
        # 2. Ders:
        zaman0847 = request.POST['zaman0847']
        zaman0850 = request.POST['zaman0850']
        zaman0930 = request.POST['zaman0930']
        # 3. Ders:
        zaman0937 = request.POST['zaman0937']
        zaman0940 = request.POST['zaman0940']
        zaman1020 = request.POST['zaman1020']
        # 4. Ders:
        zaman1027 = request.POST['zaman1027']
        zaman1030 = request.POST['zaman1030']
        zaman1110 = request.POST['zaman1110']
        # 5. Ders:
        zaman1117 = request.POST['zaman1117']
        zaman1120 = request.POST['zaman1120']
        zaman1200 = request.POST['zaman1200']
        # 6. Ders:
        zaman1257 = request.POST['zaman1257']
        zaman1300 = request.POST['zaman1300']
        zaman1340 = request.POST['zaman1340']
        # 7. Ders:
        zaman1347 = request.POST['zaman1347']
        zaman1350 = request.POST['zaman1350']
        zaman1430 = request.POST['zaman1430']
        # 8. Ders:
        zaman1437 = request.POST['zaman1437']
        zaman1440 = request.POST['zaman1440']
        zaman1520 = request.POST['zaman1520']
        # 9. Ders:
        zaman1527 = request.POST['zaman1527']
        zaman1530 = request.POST['zaman1530']
        zaman1610 = request.POST['zaman1610']
        # 10. Ders:
        zaman1617 = request.POST['zaman1617']
        zaman1620 = request.POST['zaman1620']
        zaman1700 = request.POST['zaman1700']
        # 11. Ders:
        zaman1707 = request.POST['zaman1707']
        zaman1710 = request.POST['zaman1710']
        zaman1750 = request.POST['zaman1750']
        # 12. Ders:
        zaman1757 = request.POST['zaman1757']
        zaman1800 = request.POST['zaman1800']
        zaman1840 = request.POST['zaman1840']
        # 13. Ders:
        zaman1847 = request.POST['zaman1847']
        zaman1850 = request.POST['zaman1850']
        zaman1930 = request.POST['zaman1930']
        # 14. Ders:
        zaman1937 = request.POST['zaman1937']
        zaman1940 = request.POST['zaman1940']
        zaman2020 = request.POST['zaman2020']
        # veritabnı güncellemesi
        SaatModel.objects.filter(id=1).update(ogrenci=zaman0745,ogretmen=zaman0756,cikis=zaman0759,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=2).update(ogrenci=zaman0757,ogretmen=zaman0800,cikis=zaman0840,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=3).update(ogrenci=zaman0847,ogretmen=zaman0850,cikis=zaman0930,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=4).update(ogrenci=zaman0937,ogretmen=zaman0940,cikis=zaman1020,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=5).update(ogrenci=zaman1027,ogretmen=zaman1030,cikis=zaman1110,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=6).update(ogrenci=zaman1117,ogretmen=zaman1120,cikis=zaman1200,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=7).update(ogrenci=zaman1257,ogretmen=zaman1300,cikis=zaman1340,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=8).update(ogrenci=zaman1347,ogretmen=zaman1350,cikis=zaman1430,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=9).update(ogrenci=zaman1437,ogretmen=zaman1440,cikis=zaman1520,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=10).update(ogrenci=zaman1527,ogretmen=zaman1530,cikis=zaman1610,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=11).update(ogrenci=zaman1617,ogretmen=zaman1620,cikis=zaman1700,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=12).update(ogrenci=zaman1707,ogretmen=zaman1710,cikis=zaman1750,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=13).update(ogrenci=zaman1757,ogretmen=zaman1800,cikis=zaman1840,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=14).update(ogrenci=zaman1847,ogretmen=zaman1850,cikis=zaman1930,sesDuzeyi=sesseviyesi)
        SaatModel.objects.filter(id=15).update(ogrenci=zaman1937,ogretmen=zaman1940,cikis=zaman2020,sesDuzeyi=sesseviyesi)
        messages.add_message(request, messages.SUCCESS, 'Giriş-çıkış ders saatleri ayarlandı.')    
    return render(request, 'pages/saatler.html')

def melodiler(request):
    return render(request,'pages/melodiler.html')

def duyuru(request):
    data = {
        "DuyuruMesaj": DuyuruModel.objects.all()
    }
    return render(request,'pages/duyuru.html',data)

def duyurudetails(request, id):
    data = {
        "DuyuruMesaj": DuyuruModel.objects.get(id=id)
    }
    metin=request.POST.get('mesaj',False)
    if metin:
        speech=gTTS(text=metin,lang='tr', slow=False)
        speech.save("duyuru.mp3")
        mixer.music.load("duyuru.mp3") 
        mixer.music.set_volume(0.1)
        mixer.music.play()
        
    return render(request, "pages/details.html", data)

def ogrencizilical(request):
    mixer.music.load("static/muzik/Ses/muzik1.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')
    
def durdur(request):
    mixer.music.stop()
    return render(request,'pages/hemencal.html')

def ogretmenzilical(request):
    mixer.music.load("static/muzik/Ses/muzik2.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def cikiszili(request):
    mixer.music.load("static/muzik/Ses/muzik3.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def istiklalmarsi(request):
    mixer.music.load("static/muzik/Resmi/istiklalmarsi.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def saygidurusu1(request):
    mixer.music.load("static/muzik/Resmi/saygi1dakika-istiklalmarsi.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def saygidurusu2(request):
    mixer.music.load("static/muzik/Resmi/saygi2dakika-istiklalmarsi.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')

def siren(request):
    mixer.music.load("static/muzik/Resmi/siren30saniye.mp3") 
    mixer.music.set_volume(0.1)
    mixer.music.play()
    return render(request,'pages/hemencal.html')