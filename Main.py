# Main.py için;
# • İlgili yerlerde try/except kullanılmalıdır.
# • Sadece insan sınıfı için 2 nesne üretilmelidir ve bilgiler __str__ metotu aracılığıyla yazdırılmalıdır.
# • İşsiz sınıfı için 3 nesne üretilmelidir ve __str__ metotu ile ilgili bilgiler ekrana yazdırılmalıdır.
# • Çalışan sınıfı için 3 nesne üretilmelidir ve __str__ metotu ile ilgili bilgiler ekrana yazdırılmalıdır.
# • Mavi yaka sınıfı için 3 nesne üretilmelidir ve __str__ metotu ile ilgili bilgiler ekrana yazdırılmalıdır.
# • Beyaz yaka sınıfı için 3 nesne üretilmelidir ve __str__ metotu ile ilgili bilgiler ekrana yazdırılmalıdır.
# Çalışan, mavi yaka ve beyaz yaka nesnelerinin tüm değerlerinden (“çalışan, mavi yaka, beyaz yaka” nesne değeri ,tc_no, ad, soyad, yas, cinsiyet, uyruk, sektör, tecrübe (kaydederken yıla çeviriniz), maaş, yıpranma payı, teşvik primi, yeni maaş) bir pandas DataFrame oluşturunuz (excel, csv veya dictionary ile). Oluşturduğunuz DataFrame ile şu işlemleri gerçekleştiriniz:
# a) Bazı değişken değerleri diğer nesneler için boş olabilir, DataFrame için bu değerleri 0 atayınız.
# b) Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını her grup için hesaplayınız ve yazdırınız.
# c) Maaşı 15000TL üzerinde olanların toplam sayısını bulunuz.
# d) Yeni maaşa göre DataFrame’i küçükten büyüğe sıralayınız ve yazdırınız.
# e) Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulunuz ve yazdırınız.
# f) Yeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc_no ve yeni_maaş sütunlarını seçerek gösteriniz ve yazdırınız.
# g) Var olan DataFrame’den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame elde ediniz ve yazdırınız.
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd
def main():
    insn1 = Insan("1", "Saner", "Evcin", 42, "Erkek", "Türk")
    insn2 = Insan("2", "Bade", "Ünay", 22, "Kadın", "Türk")
    issz1 = Issiz("3", "Cumhur", "Yakar", 25, "Erkek", "Türk", {"mavi": 4, "beyaz": 2, "yon": 0})
    issz2 = Issiz("4", "Vildan", "Göğebakan", 35, "Kadın", "Türk", {"mavi": 2, "beyaz": 4, "yon": 10})
    issz3 = Issiz("5", "Yıldırım", "Aşan", 51, "Erkek", "Türk", {"mavi": 10, "beyaz": 12, "yon": 0})
    cal1 = Calisan("6", "Nezih", "Kızmazoğlu", 20, "Erkek", "Türk", "Teknoloji", 22, 21000)
    cal2 = Calisan("7", "Toyanç", "Güçlü", 19, "Erkek", "Türk", "İnşaat", 13, 9000)
    cal3 = Calisan("8", "Efe", "Uzunçakmak", 45, "Erkek", "Türk", "Muhasebe", 66, 19000)
    mvyk1 = MaviYaka("9", "Emir", "Turhan", 18, "Erkek", "Türk", "İnşaat", 10000, 5, 0.2)
    mvyk2 = MaviYaka("10", "Funda", "Atbinici", 29, "Kadın", "Türk", "Muhasebe", 12000, 15, 0.4)
    mvyk3 = MaviYaka("11", "Gül", "Avcı", 31, "Kadın", "Türk", "Diğer", 19000, 29, 0.8)
    byzk1 = BeyazYaka("12", "Beyza", "Yılmaz", 26, "Kadın", "Türk", "Diğer", 14000, 19, 2000)
    byzk2 = BeyazYaka("13", "Tevfik", "Uzunoğlu", 40, "Erkek", "Türk", "Teknoloji", 21000, 22, 2500)
    byzk3 = BeyazYaka("14", "İsa", "Yılmaz", 50, "Erkek", "Türk", "Muhasebe", 19000, 35, 3000)
    print(insn1)
    print(insn2)
    print(issz1)
    print(issz2)
    print(issz3)
    print(cal1)
    print(cal2)
    print(cal3)
    print(mvyk1)
    print(mvyk2)
    print(mvyk3)
    print(byzk1)
    print(byzk2)
    print(byzk3)
    nesneler = ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"]
    kimlikler = [cal1.getkimlik(), cal2.getkimlik(), cal3.getkimlik(), mvyk1.getkimlik(), mvyk2.getkimlik(), mvyk3.getkimlik(), byzk1.getkimlik(), byzk2.getkimlik(), byzk3.getkimlik()]
    adlar = [cal1.getadi(), cal2.getadi(), cal3.getadi(), mvyk1.getadi(), mvyk2.getadi(), mvyk3.getadi(), byzk1.getadi(), byzk2.getadi(), byzk3.getadi()]
    soyadlar = [cal1.getsoyadi(), cal2.getsoyadi(), cal3.getsoyadi(), mvyk1.getsoyadi(), mvyk2.getsoyadi(), mvyk3.getsoyadi(), byzk1.getsoyadi(), byzk2.getsoyadi(), byzk3.getsoyadi()]
    yaslar = [cal1.getyasi(), cal2.getyasi(), cal3.getyasi(), mvyk1.getyasi(), mvyk2.getyasi(), mvyk3.getyasi(), byzk1.getyasi(), byzk2.getyasi(), byzk3.getyasi()]
    cinsiyetler = [cal1.getcinsiyeti(), cal2.getcinsiyeti(), cal3.getcinsiyeti(), mvyk1.getcinsiyeti(), mvyk2.getcinsiyeti(), mvyk3.getcinsiyeti(), byzk1.getcinsiyeti(), byzk2.getcinsiyeti(), byzk3.getcinsiyeti()]
    uyruklar = [cal1.getuyruk(), cal2.getuyruk(), cal3.getuyruk(), mvyk1.getuyruk(), mvyk2.getuyruk(), mvyk3.getuyruk(), byzk1.getuyruk(), byzk2.getuyruk(), byzk3.getuyruk()]
    sektorler = [cal1.getsektoru(), cal2.getsektoru(), cal3.getsektoru(), mvyk1.getsektoru(), mvyk2.getsektoru(), mvyk3.getsektoru(), byzk1.getsektoru(), byzk2.getsektoru(), byzk3.getsektoru()]
    maaslar = [cal1.getmaasi(), cal2.getmaasi(), cal3.getmaasi(), mvyk1.getmaasi(), mvyk2.getmaasi(), mvyk3.getmaasi(), byzk1.getmaasi(), byzk2.getmaasi(), byzk3.getmaasi()]
    primler = [0, 0, 0, 0, 0, 0, byzk1.gettesvik_primi(), byzk2.gettesvik_primi(), byzk3.gettesvik_primi()]
    yipranmalar = [0, 0, 0, mvyk1.getyipranmapayi(), mvyk2.getyipranmapayi(), mvyk3.getyipranmapayi(), 0, 0, 0]
    yeni_maaslar = [cal1.getmaasi() + cal1.getmaasi()*cal1.zam_hakki(), cal2.getmaasi() + cal2.getmaasi()*cal2.zam_hakki(), cal3.getmaasi() + cal3.getmaasi()*cal3.zam_hakki(), mvyk1.getmaasi() + mvyk1.getmaasi()*mvyk1.zam_hakki(), mvyk2.getmaasi() + mvyk2.getmaasi()*mvyk2.zam_hakki(), mvyk3.getmaasi() + mvyk3.getmaasi()*mvyk3.zam_hakki(), byzk1.getmaasi() + byzk1.zam_hakki(), byzk2.getmaasi() + byzk2.zam_hakki(), byzk3.getmaasi() + byzk3.zam_hakki()]
    tablo = pd.DataFrame({"Nesne": nesneler, "Kimlik": kimlikler, "Ad": adlar, "Soyad": soyadlar, "Yaş": yaslar, "Cinsiyet": cinsiyetler, "Uyruk": uyruklar, "Sektör": sektorler, "Maaş": maaslar, "Prim": primler, "Yıpranma Payı": yipranmalar, "Yeni Maaş": yeni_maaslar})
    print(tablo)
    print("Maaşı 15000TL üzerinde olanların toplam sayısı: ", len(tablo[tablo["Maaş"] > 15000]))
    print(tablo.sort_values(by = "Yeni Maaş"))
