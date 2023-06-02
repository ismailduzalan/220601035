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
def main():
    insn1 = Insan("1", "Saner", "Evcin", 42, "Erkek", "Türk")
    insn2 = Insan("2", "Bade", "Ünay", 22, "Kadın", "Türk")
    issz1 = Issiz("3", "Cumhur", "Yakar", 25, "Erkek", "Türk", {"mavi": 4, "beyaz": 2, "yon": 0})
    issz2 = Issiz("4", "Vildan", "Göğebakan", 35, "Kadın", "Türk", {"mavi": 2, "beyaz": 4, "yon": 10})
    issz3 = Issiz("5", "Yıldırım", "Aşan", 51, "Erkek", "Türk", {"mavi": 10, "beyaz": 12, "yon": 0})
    print(insn1)
    print(insn2)
    print(issz1)
    print(issz2)
    print(issz3)
