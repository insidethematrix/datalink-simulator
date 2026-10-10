# error_control.py
# Hata kontrolü modülü: Parity (eşlik biti) ve CRC (döngüsel artıklık denetimi).
# Gönderici veriye birkaç "kontrol biti" ekler, alıcı bu bitlere bakarak
# kanalda hata olup olmadığını anlamaya çalışır.

# CRC polinomları bit listesi olarak tutulur (en yüksek dereceden başlayarak).
# CRC-8: x^8 + x^2 + x + 1  ->  1 0000 0111
CRC8_POLY = [1, 0, 0, 0, 0, 0, 1, 1, 1]

# Elle hesap yapıp anlamak için küçük bir polinom: x^3 + x + 1  ->  1011
CRC3_POLY = [1, 0, 1, 1]


# ---------------------------------------------------------------------------
# PARITY
# ---------------------------------------------------------------------------

# Verinin parity bitini hesaplar.
# "even" (çift): 1'lerin toplam sayısı (parity dahil) çift olacak şekilde bit seçilir.
# "odd"  (tek) : 1'lerin toplam sayısı (parity dahil) tek olacak şekilde bit seçilir.
# Örnek: compute_parity_bit([1, 0, 1, 1], "even") -> 1  (üç tane 1 var, dördüncüyü ekle)
#        compute_parity_bit([1, 0, 1, 1], "odd")  -> 0
def compute_parity_bit(bits, mode="even"):
    ones_count = 0
    for bit in bits:
        if bit == 1:
            ones_count += 1

    if mode == "even":
        return ones_count % 2
    elif mode == "odd":
        return 1 - (ones_count % 2)
    else:
        raise ValueError("Parity türü 'even' veya 'odd' olmalı.")


# Verinin sonuna parity bitini ekleyip gönderilecek çerçeveyi döndürür.
# Örnek: add_parity([1, 0, 1, 1], "even") -> [1, 0, 1, 1, 1]
def add_parity(bits, mode="even"):
    return bits + [compute_parity_bit(bits, mode)]


# Alıcı tarafı: çerçevenin parity'si doğru mu?
# Doğruysa True (hata görülmedi), yanlışsa False (hata var) döndürür.
# Örnek: check_parity([1, 0, 1, 1, 1], "even") -> True
#        check_parity([1, 0, 0, 1, 1], "even") -> False  (bir bit bozulmuş)
def check_parity(frame, mode="even"):
    data = frame[:-1]
    received_parity = frame[-1]
    return compute_parity_bit(data, mode) == received_parity


# ---------------------------------------------------------------------------
# CRC
# ---------------------------------------------------------------------------

# Bitleri polinoma "XOR bölmesi" ile böler ve kalanı döndürür.
# Kalanın uzunluğu her zaman len(poly) - 1'dir.
# Örnek (elle takip edilebilir):
#   crc_remainder([1, 1, 0, 1, 0, 0, 0], [1, 0, 1, 1]) -> [0, 0, 1]
#   (1101 verisine 3 sıfır eklenmiş hali, 1011 ile bölünüyor)
def crc_remainder(bits, poly):
    # Gelen listeyi bozmamak için kopyasıyla çalışıyoruz.
    remainder = list(bits)

    # Polinom, listenin dışına taşmadığı son konuma kadar sağa kaydırılır.
    # Örn. 7 bit ve 4 bitlik polinom için i = 0, 1, 2, 3
    for i in range(len(remainder) - len(poly) + 1):
        # Baştaki bit 0 ise bu hizada bölme yapılmaz, bir sağa geçilir.
        if remainder[i] == 1:
            # Polinomu i konumuna hizala ve her bitini alttaki bitle XOR'la.
            for j in range(len(poly)):
                remainder[i + j] = remainder[i + j] ^ poly[j]

    # Bölme bitti; kalan, listenin son (len(poly) - 1) biti.
    degree = len(poly) - 1
    return remainder[len(remainder) - degree:]


# Gönderici tarafı: verinin sonuna CRC kalanını ekleyip çerçeveyi döndürür.
# Adımlar: 1) veriye (polinom derecesi kadar) sıfır ekle
#          2) bu uzun diziyi polinoma böl, kalanı bul
#          3) sıfırların yerine kalanı koy (veri + kalan)
# Örnek: add_crc([1, 1, 0, 1], [1, 0, 1, 1]) -> [1, 1, 0, 1, 0, 0, 1]
def add_crc(bits, poly=CRC8_POLY):
    degree = len(poly) - 1
    padded_data = bits + [0] * degree
    remainder = crc_remainder(padded_data, poly)
    return bits + remainder


# Alıcı tarafı: gelen çerçeveyi (veri + kalan) aynı polinoma böler.
# Kalan tamamen sıfırsa True (hata görülmedi), değilse False (hata var).
# Örnek: check_crc([1, 1, 0, 1, 0, 0, 1], [1, 0, 1, 1]) -> True
def check_crc(frame, poly=CRC8_POLY):
    remainder = crc_remainder(frame, poly)
    return 1 not in remainder
