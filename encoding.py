# encoding.py
# Metin <-> bit dönüşümü yapan modül.
# Bitler, 0 ve 1'lerden oluşan bir tamsayı listesi olarak tutulur.
# Örnek: "A" -> [0, 1, 0, 0, 0, 0, 0, 1]


# Metni bit listesine çevirir.
# Önce metin UTF-8 ile baytlara çevrilir, sonra her bayt 8 bite açılır.
# Örnek: "A" -> [0, 1, 0, 0, 0, 0, 0, 1]
def metni_bitlere_cevir(metin):
    bayt_listesi = metin.encode("utf-8")
    bitler = []
    for bayt in bayt_listesi:
        # format(65, "08b") -> "01000001" (8 haneli, başı sıfırla doldurulmuş)
        ikili_yazi = format(bayt, "08b")
        for karakter in ikili_yazi:
            bitler.append(int(karakter))
    return bitler


# 8 elemanlı bir bit listesini tek bir sayıya (0-255) çevirir.
# Örnek: [0, 1, 0, 0, 0, 0, 0, 1] -> 65
def sekiz_biti_sayiya_cevir(sekiz_bit):
    # Her bit, kendi basamak değeriyle (128, 64, ..., 1) çarpılıp toplanır.
    sayi = 0
    for index, bit in enumerate(sekiz_bit):
        sayi += bit * (2 ** (7 - index))
    return sayi


# Bit listesini tekrar metne çevirir.
# Bitler 8'erli gruplara ayrılır, her grup bir bayta, baytlar da metne dönüşür.
# Örnek: [0, 1, 0, 0, 0, 0, 0, 1] -> "A"
def bitleri_metne_cevir(bitler):
    if len(bitler) % 8 != 0:
        raise ValueError("Bit sayısı 8'in katı olmalı.")

    bayt_listesi = []
    # 8'er 8'er grupla
    for i in range(0, len(bitler), 8):
        sekiz_bit = bitler[i:i + 8]
        bayt_listesi.append(sekiz_biti_sayiya_cevir(sekiz_bit))

    # errors="replace": Kanalda bozulan bitler geçersiz bir UTF-8 baytı
    # oluşturursa program çökmez, o karakterin yerine "�" yazılır.
    return bytes(bayt_listesi).decode("utf-8", errors="replace")
