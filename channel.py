# channel.py
# Gürültülü kanal modülü.
# Her bit, diğerlerinden bağımsız olarak "hata_olasiligi" ile ters çevrilir (0 <-> 1).
# Bu modele "Binary Symmetric Channel" (BSC) denir.

import random


# Bitleri gürültülü kanaldan geçirir ve alıcıya ulaşan bitleri döndürür.
# Gönderilen liste değiştirilmez, yeni bir liste oluşturulur.
# seed verilirse aynı girdi her seferinde aynı sonucu verir (test ve sunum için).
# Örnek: kanaldan_gecir([0, 1, 0, 1], 0.0) -> [0, 1, 0, 1]  (hiç hata yok)
#        kanaldan_gecir([0, 1, 0, 1], 1.0) -> [1, 0, 1, 0]  (her bit bozulur)
def kanaldan_gecir(bitler, hata_olasiligi, seed=None):
    if hata_olasiligi < 0 or hata_olasiligi > 1:
        raise ValueError("Hata olasılığı 0 ile 1 arasında olmalı.")

    # Kendi rastgele sayı üretecimiz; rastgele.random() 0 ile 1 arasında sayı verir.
    rastgele = random.Random(seed)
    alinan_bitler = []

    # Her bit için bir sayı çekilir; sayı hata_olasiligi'ndan küçükse bit bozulur.
    for bit in bitler:
        rastgele_sayi = rastgele.random()
        if rastgele_sayi >= hata_olasiligi:
            alinan_bitler.append(bit)
        else:
            alinan_bitler.append(1 - bit)

    return alinan_bitler


# Gönderilen ve alınan bitleri karşılaştırır, farklı olan konumları döndürür.
# Örnek: hatali_konumlari_bul([0, 1, 0, 1], [0, 0, 0, 1]) -> [1]
def hatali_konumlari_bul(gonderilen, alinan):
    konumlar = []
    for i in range(len(gonderilen)):
        if gonderilen[i] != alinan[i]:
            konumlar.append(i)
    return konumlar
