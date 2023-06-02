# İnsan sınıfında (Insan.py); tc_no, ad, soyad, yaş, cinsiyet, uyruk bilgileri private değişkenleri olarak bulunmalıdır.
# • Değişkenlere göre Initializer metot olmalıdır.
# • Tüm değişkenler için get/set metotları tanımlanmalıdır.
# • __str__ metotu ile kullanıcı bilgileri yazdırılmalıdır.
class Insan: #insan sınıfı oluşturuldu
    def __init__(self,kimlik,adi,soyadi,yasi,cinsiyeti,uyruk): #insan sınıfının özellikleri tanımlandı
        # private değişkenler tanımlandı
        self.__kimlik=kimlik 
        self.__adi=adi
        self.__soyadi=soyadi
        self.__yasi=yasi
        self.__cinsiyeti=cinsiyeti
        self.__uyruk=uyruk
    def __str__(self): #insan sınıfının özellikleri yazdırıldı
        return "Kimlik: {}\nAdı: {}\nSoyadı: {}\nYaşı: {}\nCinsiyeti: {}\nUyruk: {}\n".format(self.__kimlik,self.__adi,self.__soyadi,self.__yasi,self.__cinsiyeti,self.__uyruk)
    # get ve set metotları tanımlandı
    def getkimlik(self): 
        return self.__kimlik
    def setkimlik(self,tc_no):
        self.__kimlik=tc_no
    def getadi(self):
        return self.__adi
    def setadi(self,ad):
        self.__adi=ad
    def getsoyadi(self):
        return self.__soyadi
    def setsoyadi(self,soyad):
        self.__soyadi=soyad
    def getyasi(self):
        return self.__yasi
    def setyasi(self,yas):
        self.__yasi=yas
    def getcinsiyeti(self):

        return self.__cinsiyeti
    def setcinsiyeti(self,cinsiyet):
        self.__cinsiyeti=cinsiyet
    def getuyruk(self):
        return self.__uyruk
    def setuyruk(self,uyruk):
        self.__uyruk=uyruk





        