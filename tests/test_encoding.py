# encoding.py modülünün testleri.
import pytest

from encoding import text_to_bits, bits_to_text, byte_to_int


# "A" harfinin kodu 65'tir, ikili hali 01000001.
def test_letter_to_bits():
    assert text_to_bits("A") == [0, 1, 0, 0, 0, 0, 0, 1]


# Sekiz bitin sayıya çevrilmesi (A, en küçük ve en büyük değer).
def test_byte_to_int():
    assert byte_to_int([0, 1, 0, 0, 0, 0, 0, 1]) == 65
    assert byte_to_int([0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert byte_to_int([1, 1, 1, 1, 1, 1, 1, 1]) == 255


# Gidiş-dönüş: metin -> bit -> metin aynı sonucu vermeli (Türkçe harfler dahil).
def test_round_trip():
    text = "Veri iletişimi ğüşıöç"
    assert bits_to_text(text_to_bits(text)) == text


# 8'in katı olmayan bit sayısı hata vermeli.
def test_incomplete_bits_raise_error():
    with pytest.raises(ValueError):
        bits_to_text([0, 1, 0])
