# Mavi yaka sınıfı için (MaviYaka.py) yıpranma payı (float: 0.2, 0.5 gibi değer almalıdır) değişkeni private olarak bulunmalıdır.
# • Değişkenlere göre Initializer metot olmalıdır.
# • Tüm gerekli değişkenler için get/set metotları tanımlanmalıdır.
# • Çalışanın zam hakkını hesaplayan zam_hakki metodu yazılacaktır (2 sene öncesi tecrübesi olanın zam oranı önerisi “yıpranma_payi*10” olacaktır. 2-4 sene arası çalışan ise ve maaş 15000TL altıysa “(maaş%tecrübe)/2 + (yıpranma_payi*10)” sonucu zam oranı önerilecektir. 4 seneden fazla tecrübe varsa ve maaş 25000 altıysa “(maaş%tecrübe)/3+ (yıpranma_payi*10)” zam oranı önerilecektir). Yeni maaş, eski maaş ile aynıysa eski maaş, yeni maaşa atanmalıdır.
# • İlgili yerlerde try/except kullanılmalıdır.
# • __str__ metotunda ad, soyad, tecrübe ve yeni maaşı (public değişken ile yazdırılmamalı) yazılmalıdır.
from Calisan import Calisan
class MaviYaka(Calisan): # Calisan class'ından MaviYaka class'ı türetildi.
    def __init__(self, kimlik, adi, soyadi, yasi, cinsiyeti, uyruk, sektoru, maasi, tecrubesi, yipranma_payi): # MaviYaka class'ının özellikleri tanımlandı.
        super().__init__(kimlik,adi,soyadi,yasi,cinsiyeti,uyruk,sektoru,tecrubesi,maasi) # Calisan class'ının özellikleri MaviYaka class'ına aktarıldı.
        # private değişkenler tanımlandı.
        self.__yipranma_payi = yipranma_payi
    # get ve set metotları tanımlandı.
    def getyipranmapayi(self):
        return self.__yipranma_payi
    def setyipranmapayi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi
    def zam_hakki(self): # zam_hakki metodu tanımlandı.
        try:
            zam = 0
            if self.gettecrubesi() < 24: # 2 sene öncesi tecrübesi olanın zam oranı önerisi “yıpranma_payi*10” olacaktır.
                zam = self.__yipranma_payi * 10
            elif self.gettecrubesi() >= 24 and self.gettecrubesi() <= 48 and self.getmaasi() < 15000: # Tecrübesi 2-4 sene arası çalışan ise ve maaş 15000TL altıysa “(maaş%tecrübe)/2 + (yıpranma_payi*10)” sonucu zam oranı önerilecektir.
                zam = (self.getmaasi() % self.gettecrubesi()) / 2 + self.__yipranma_payi * 10 
            elif self.gettecrubesi() > 48 and self.getmaasi() < 25000: # Tecrübesi 4 seneden fazla varsa ve maaş 25000 altıysa “(maaş%tecrübe)/3 + (yıpranma_payi*10)” zam oranı önerilecektir.
                zam =( self.getmaasi() % self.gettecrubesi() )/3 + self.__yipranma_payi * 10
            else:
                zam = 0
        except Exception as hata:
            print("Hatalı giriş yaptınız." + str(hata))
            zam = 0
        return zam / 100