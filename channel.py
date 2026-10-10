# channel.py
# Gürültülü kanal modülü.
# Her bit, diğerlerinden bağımsız olarak "error_rate" olasılığıyla ters çevrilir (0 <-> 1).
# Bu modele "Binary Symmetric Channel" (BSC) denir.

import random


# Bitleri gürültülü kanaldan geçirir ve alıcıya ulaşan bitleri döndürür.
# Gönderilen liste değiştirilmez, yeni bir liste oluşturulur.
# seed verilirse aynı girdi her seferinde aynı sonucu verir (test ve sunum için).
# Örnek: transmit([0, 1, 0, 1], 0.0) -> [0, 1, 0, 1]  (hiç hata yok)
#        transmit([0, 1, 0, 1], 1.0) -> [1, 0, 1, 0]  (her bit bozulur)
def transmit(bits, error_rate, seed=None):
    if error_rate < 0 or error_rate > 1:
        raise ValueError("Hata olasılığı 0 ile 1 arasında olmalı.")

    # Kendi rastgele sayı üretecimiz; rng.random() 0 ile 1 arasında sayı verir.
    rng = random.Random(seed)
    received_bits = []

    # Her bit için bir sayı çekilir; sayı error_rate'ten küçükse bit bozulur.
    for bit in bits:
        random_number = rng.random()
        if random_number >= error_rate:
            received_bits.append(bit)
        else:
            received_bits.append(1 - bit)

    return received_bits


# Gönderilen ve alınan bitleri karşılaştırır, farklı olan konumları döndürür.
# Örnek: find_error_positions([0, 1, 0, 1], [0, 0, 0, 1]) -> [1]
def find_error_positions(sent, received):
    positions = []
    for i in range(len(sent)):
        if sent[i] != received[i]:
            positions.append(i)
    return positions
