# PARDUS ETAP İÇİN OKUL ZİLİ VE DUYURU SİSTEMİ

**PROJE AMACI:**

 Hayatın her alanında her gün yeni fonksiyonlarla karşımıza çıkan teknoloji, hayatı kolaylaştırıp güncel yaşamın yoğunluğunda işlerin olabildiğince pratik olmasını sağlamaktadır. Bizler de okulumuzda bu anlamda zil sistemiyle ilgili yapabileceklerimizi düşündük ve belirli kişilere yetki verildiği takdirde herhangi bir cihazdan kontrol edilmesi mümkün olan zil ve duyuru otomasyonunu gerçekleştirmeyi amaçladık.

**PROJE YÖNTEMİ:**
 Bu proje için öncelikle benzer uygulamalar ve işleyiş şekilleri incelenecektir. Sonrasında okul içindeki ağdan, herhangi bir cihaz üzerinden web arayüzüne giriş için bir web sayfası yapılacaktır. Güvenlik, mobil sistem üzerinden kontrol ve kumanda, veri yükleme ve girilen duyuru metinlerinin Google API'yle sese dönüştürülmesi gibi özellikler sağlanacaktır. Bunlar için donanım olarak Pardus ETAP kurulu akıllı tahta, programlama için Python, Django, veritabanı için SQLite3, arayüz tasarımı için HTML, CSS, JavaScript, python modülleri için de gTTS, pygame, os, system kullanılacaktır.

**BEKLENEN SONUÇ:** 
Mevcut zil ve duyuru sistemlerinin, teknolojinin hızına ayak uydurması şeklinde tanımlanabilecek olan bu proje,okulumuz zil ve duyuru sisteminin daha etkili ve pratik kullanımını sağlayacaktır. Milli Eğitim Bakanlığına bağlı okullar ve ETAP kurulmuş akıllı tahtalara kurulumlar yapıldığı takdirde tüm okullar da GitHub'da açık kaynak olarak dağıtılacak olan bu yazılımdan faydalanabileceklerdir. İstenildiği takdirde diğer resmi kurumlar ve işyerleri için de uyarlanabileceğinin imkanı gösterilecektir.

**GÖREV DAĞILIMI:**

**Danışman Öğretmen:** Nuri TIRAŞ

**Öğrenciler:** Adem KARPUZ, Metehan GÖKYOKUŞ, Ali Nail ACAR

**Kurulum:**  
mkdir etap  
cd etap  
sudo apt-get install git  
git clone  https://github.com/nuritiras/Etap-Zil.git  
sudo apt install python3-pip  
sudo apt install python3-venv  
python3 -m venv env  
source env/bin/activate  
cd Etap-Zil  
pip install -r requirements.txt  
python3 manage.py runserver 0.0.0.0:8000  

**Kullanıcı adı:** admin  
**Şifre:** etap.2022  

**Kaynak:**  

https://gonullu.pardus.org.tr/pardus-21de-vscode-ile-python-gelistirme-ortaminin-hazirlanmasi/

https://gonullu.pardus.org.tr/pardus-21-ile-python-django-kutuphanesine-giris/
