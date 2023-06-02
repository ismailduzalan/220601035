# Çalışan sınıfı için (Calisan.py) sektör (kullanıcının “teknoloji, muhasebe, inşaat, diğer” seçenekleri girmesi sağlanmalı ve doğru girdiği kontrol edilmelidir), tecrübe (ay değeri) ve maaş değişkenleri private olarak tanımlanmalıdır.
# • Değişkenlere göre Initializer metot olmalıdır.
# • Tüm gerekli değişkenler için get/set metotları tanımlanmalıdır.
# • Çalışanın zam hakkını hesaplayan zam_hakki metodu yazılacaktır (2 sene öncesi tecrübesi olanın zam oranı önerisi 0’dır. 2-4 sene arası çalışan ise ve maaş 15000TL altıysa “maaş%tecrübe” sonucu zam oranı önerilecektir. 4 seneden fazla tecrübe varsa ve maaş 25000 altıysa “(maaş%tecrübe)/2” zam oranı önerilecektir). Yeni maaş, eski maaş ile aynıysa eski maaş, yeni maaşa atanmalıdır.
# • İlgili yerlerde try/except kullanılmalıdır.
# • __str__ metotunda ad, soyad, tecrübe ve yeni maaşı (public değişken ile yazdırılmamalı) yazılmalıdır.
from Insan import Insan # Insan.py dosyasından Insan class.
class Calisan(Insan): # Insan class'ından Calisan class'ı türetildi.
    def __init__(self, kimlik, adi, soyadi, yasi, cinsiyeti, uyruk, sektor, tecrube, maasi): # Calisan class'ının özellikleri tanımlandı.
        super().__init__(kimlik,adi,soyadi,yasi,cinsiyeti,uyruk) # Insan class'ının özellikleri Calisan class'ına aktarıldı.
        # private değişkenler tanımlandı.
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maasi
    def __str__(self): # Calisan class'ının özellikleri yazdırıldı.
        return super().__str__() + "Sektörü: " + self.__sektor + "\nTecrübesi: " + str(self.__tecrube) + "\nYeni Maaşı: " + str(self.__maas + self.zam_hakki() * self.__maas) + " TL\n"
    # get ve set metotları tanımlandı.
    def getsektoru(self):
        return self.__sektor
    def setsektoru(self, sektor):
        self.__sektor = sektor
    def gettecrubesi(self):
        return self.__tecrube
    def settecrubesi(self, tecrube):
        self.__tecrube = tecrube
    def getmaasi(self):
        return self.__maas
    def setmaasi(self, maas):
        self.__maas = maas
