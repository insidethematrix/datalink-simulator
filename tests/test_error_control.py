# error_control.py modülünün testleri.
import pytest

from encoding import text_to_bits
from error_control import (
    CRC3_POLY,
    CRC8_POLY,
    compute_parity_bit,
    add_parity,
    check_parity,
    crc_remainder,
    add_crc,
    check_crc,
)


# ---------------------------------------------------------------------------
# PARITY
# ---------------------------------------------------------------------------

# Üç tane 1 var: çift parity 1, tek parity 0 olmalı.
def test_compute_parity_bit():
    assert compute_parity_bit([1, 0, 1, 1], "even") == 1
    assert compute_parity_bit([1, 0, 1, 1], "odd") == 0


# Parity bit verinin sonuna eklenmeli.
def test_add_parity():
    assert add_parity([1, 0, 1, 1], "even") == [1, 0, 1, 1, 1]


# Gelen veri listesi değiştirilmemeli.
def test_add_parity_does_not_modify_input():
    data = [1, 0, 1, 1]
    add_parity(data)
    assert data == [1, 0, 1, 1]


# Sağlam çerçeve kontrolden geçmeli.
def test_parity_valid_frame():
    frame = add_parity([1, 0, 1, 1], "odd")
    assert check_parity(frame, "odd") is True


# Tek bit hatası yakalanmalı.
def test_parity_detects_single_bit_error():
    frame = add_parity([1, 0, 1, 1], "even")
    frame[1] = 1 - frame[1]
    assert check_parity(frame, "even") is False


# Parity'nin zayıf yanı: iki bit bozulursa hata fark edilmez.
def test_parity_misses_two_bit_error():
    frame = add_parity([1, 0, 1, 1], "even")
    frame[0] = 1 - frame[0]
    frame[1] = 1 - frame[1]
    assert check_parity(frame, "even") is True


# Geçersiz parity türü hata vermeli.
def test_invalid_parity_mode():
    with pytest.raises(ValueError):
        compute_parity_bit([1, 0], "other")


# ---------------------------------------------------------------------------
# CRC
# ---------------------------------------------------------------------------

# Ders kitabı örneği: 1101000 / 1011 -> kalan 001
def test_crc_remainder_textbook_example():
    assert crc_remainder([1, 1, 0, 1, 0, 0, 0], CRC3_POLY) == [0, 0, 1]


# Kalanın uzunluğu polinomun derecesine eşit olmalı.
def test_crc_remainder_length():
    data = text_to_bits("Merhaba")
    assert len(add_crc(data, CRC8_POLY)) == len(data) + 8


# add_crc: veri + kalan
def test_add_crc():
    assert add_crc([1, 1, 0, 1], CRC3_POLY) == [1, 1, 0, 1, 0, 0, 1]


# Gelen veri listesi değiştirilmemeli.
def test_add_crc_does_not_modify_input():
    data = [1, 1, 0, 1]
    add_crc(data, CRC3_POLY)
    assert data == [1, 1, 0, 1]


# Sağlam çerçeve kontrolden geçmeli (gerçek bir mesajla, CRC-8).
def test_crc_valid_frame():
    frame = add_crc(text_to_bits("Merhaba"))
    assert check_crc(frame) is True


# Çerçevenin hangi biti bozulursa bozulsun, tek bit hatası yakalanmalı.
def test_crc_detects_every_single_bit_error():
    valid = add_crc(text_to_bits("Hi"))
    for i in range(len(valid)):
        corrupted = list(valid)
        corrupted[i] = 1 - corrupted[i]
        assert check_crc(corrupted) is False


# Parity'nin kaçırdığı iki bit hatasını CRC yakalamalı.
def test_crc_detects_two_bit_error():
    frame = add_crc(text_to_bits("Hi"))
    frame[0] = 1 - frame[0]
    frame[1] = 1 - frame[1]
    assert check_crc(frame) is False
