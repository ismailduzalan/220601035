# Beyaz yaka sınıfı için (BeyazYaka.py) teşvik primi (500, 2500 gibi değer almalıdır) değişkeni private olarak bulunmalıdır.
# • Değişkenlere göre Initializer metot olmalıdır.
# • Tüm gerekli değişkenler için get/set metotları tanımlanmalıdır.
# • Çalışanın zam hakkını hesaplayan zam_hakki metodu yazılacaktır (2 sene öncesi tecrübesi olanın zam önerisi “teşvik_primi” olacaktır. 2-4 sene arası çalışan ise ve maaş 15000TL altıysa “(maaş%tecrübe)*5 + teşvik_primi” sonucu, zam olarak önerilecektir (önceki sınıflar gibi oran değil, bu sınıf zam miktarı). 4 seneden fazla tecrübe varsa ve maaş 25000 altıysa “(maaş%tecrübe)*4 + teşvik_primi” zam olarak önerilecektir). Yeni maaş, eski maaş ile aynıysa eski maaş, yeni maaşa atanmalıdır.
# • İlgili yerlerde try/except kullanılmalıdır.
# • __str__ metotunda ad, soyad, tecrübe ve yeni maaşı (public değişken ile yazdırılmamalı) yazılmalıdır.
from Calisan import Calisan
class BeyazYaka(Calisan): # Calisan class'ından BeyazYaka class'ı türetildi.
    def __init__(self, kimlik, adi, soyadi, yasi, cinsiyeti, uyruk, sektoru, maasi, tecrubesi, tesvik_primi): # BeyazYaka class'ının özellikleri tanımlandı.
        super().__init__(kimlik, adi, soyadi, yasi, cinsiyeti, uyruk, sektoru, tecrubesi, maasi) # Calisan class'ının özellikleri miras alındı.
        self.__tesvik_primi = tesvik_primi # BeyazYaka class'ının özellikleri tanımlandı.
    def __str__(self): # Calisan class'ının özellikleri yazdırıldı.
        return super().__str__() + "\nSektörü: " + self.getsektoru() + "\nTecrübesi: " + str(self.gettecrubesi()) + "\nYeni Maaşı: " + str(self.getmaasi() + self.zam_hakki()) + " TL"
    def gettesvik_primi(self): # get_tesvik_primi fonksiyonu tanımlandı.
        return self.__tesvik_primi # get_tesvik_primi fonksiyonu çağırıldığında __tesvik_primi değeri döndürülecek.
    def settesvik_primi(self, tesvik_primi): # set_tesvik_primi fonksiyonu tanımlandı.
        self.__tesvik_primi = tesvik_primi # set_tesvik_primi fonksiyonu çağırıldığında __tesvik_primi değeri değiştirilecek.
    def zam_hakki(self): # zam_hakki metodu tanımlandı.
        try:
            zam = 0
            if self.gettecrubesi() < 24: # 2 sene öncesi tecrübesi olanın zam oranı önerisi  “teşvik_primi” olacaktır.
                zam = self.__tesvik_primi
            elif self.gettecrubesi() >= 24 and self.gettecrubesi() <= 48 and self.getmaasi() < 15000: # Tecrübesi 2-4 sene arası çalışan ise ve maaş 15000TL altıysa zam oranı “(maaş%tecrübe)*5 + teşvik_primi” sonucu, zam olarak önerilecektir.
                zam = ( self.getmaasi() % self.gettecrubesi() )*5 + self.__tesvik_primi 
            elif self.gettecrubesi() > 48 and self.getmaasi() < 25000: # Tecrübesi 4 seneden fazla varsa ve maaş 25000 altıysa zam oranı “(maaş%tecrübe)*4 + teşvik_primi” zam olarak önerilecektir).
                zam =( self.getmaasi() % self.gettecrubesi() )*4 + self.__tesvik_primi
            else:
                zam = 0
        except Exception as hata:
            print("Hatalı giriş yaptınız." + str(hata))
            zam = 0
        return zam