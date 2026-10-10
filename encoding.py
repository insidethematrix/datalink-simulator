# encoding.py
# Metin <-> bit dönüşümü yapan modül.
# Bitler, 0 ve 1'lerden oluşan bir tamsayı listesi olarak tutulur.
# Örnek: "A" -> [0, 1, 0, 0, 0, 0, 0, 1]


# Metni bit listesine çevirir.
# Önce metin UTF-8 ile baytlara çevrilir, sonra her bayt 8 bite açılır.
# Örnek: "A" -> [0, 1, 0, 0, 0, 0, 0, 1]
def text_to_bits(text):
    byte_list = text.encode("utf-8")
    bits = []
    for byte in byte_list:
        # format(65, "08b") -> "01000001" (8 haneli, başı sıfırla doldurulmuş)
        binary_string = format(byte, "08b")
        for char in binary_string:
            bits.append(int(char))
    return bits


# 8 elemanlı bir bit listesini tek bir sayıya (0-255) çevirir.
# Örnek: [0, 1, 0, 0, 0, 0, 0, 1] -> 65
def byte_to_int(eight_bits):
    # Her bit, kendi basamak değeriyle (128, 64, ..., 1) çarpılıp toplanır.
    number = 0
    for index, bit in enumerate(eight_bits):
        number += bit * (2 ** (7 - index))
    return number


# Bit listesini tekrar metne çevirir.
# Bitler 8'erli gruplara ayrılır, her grup bir bayta, baytlar da metne dönüşür.
# Örnek: [0, 1, 0, 0, 0, 0, 0, 1] -> "A"
def bits_to_text(bits):
    if len(bits) % 8 != 0:
        raise ValueError("Bit sayısı 8'in katı olmalı.")

    byte_list = []
    # 8'er 8'er grupla
    for i in range(0, len(bits), 8):
        eight_bits = bits[i:i + 8]
        byte_list.append(byte_to_int(eight_bits))

    # errors="replace": Kanalda bozulan bitler geçersiz bir UTF-8 baytı
    # oluşturursa program çökmez, o karakterin yerine "�" yazılır.
    return bytes(byte_list).decode("utf-8", errors="replace")
