# İşsiz sınıfı için (Issiz.py) statüsü (“mavi yaka, beyaz yaka, yönetici”) olan ve bu statülere ait geçmiş tecrübelerinin (yıl değeri) tutulduğu bir dictionary private değişkeni bulunmalıdır.
# • Değişkene göre Initializer metot olmalıdır.
# • Tüm gerekli değişkenler için get/set metotları tanımlanmalıdır.
# • En uygun statünün bulunması için statu_bul metodu yazınız (Dictionaryde girilen değerlere göre; yıl değerinde mavi yakanın etkisi %20, beyaz yakanın etkisi %35, yöneticinin etkisi %45 olarak hesaplayınız ve en yüksek çıkan değere ait statüyü ilgili değişkeninize atayınız. Bu değişkene farklı bir class’tan erişim sağlanabilmelidir.)
# • İlgili yerlerde try/except kullanılmalıdır.
# • __str__ metotu içinde kullanıcının ad, soyadı ve dictionary ile hesaplanan kişiye en uygun statü (public değişken ile yazdırılmamalı) yazdırılmalıdır.
from Insan import Insan # Insan.py dosyasından Insan class.
class Issiz(Insan): # Insan class'ından Issiz class'ı türetildi.
    def __init__(self, kimlik, adi, soyadi, yasi, cinsiyeti, uyruk, yil): # Issiz class'ının özellikleri tanımlandı.
        super().__init__(kimlik,adi,soyadi,yasi,cinsiyeti,uyruk) # Insan class'ının özellikleri Issiz class'ına aktarıldı.
        # private değişkenler tanımlandı.
        self.__yil = yil
        self__statu = ""
    def __str__(self): # Issiz class'ının özellikleri yazdırıldı.
        return super().__str__() + "Statüsü: " + self.statu_bul() + "\n"
    # get ve set metotları tanımlandı.
    def getyil(self):
        return self.__yil
    def setyil(self, yil):
        self.__yil = yil
    def getStatu(self):
        return self.__statu
    def setStatu(self, statu):
        self.__statu = statu
