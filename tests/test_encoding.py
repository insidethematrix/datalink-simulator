# encoding.py modülünün testleri.
import pytest

from encoding import metni_bitlere_cevir, bitleri_metne_cevir, sekiz_biti_sayiya_cevir


# "A" harfinin kodu 65'tir, ikili hali 01000001.
def test_harf_bitlere_cevrilir():
    assert metni_bitlere_cevir("A") == [0, 1, 0, 0, 0, 0, 0, 1]


# Sekiz bitin sayıya çevrilmesi (A, en küçük ve en büyük değer).
def test_sekiz_bit_sayiya():
    assert sekiz_biti_sayiya_cevir([0, 1, 0, 0, 0, 0, 0, 1]) == 65
    assert sekiz_biti_sayiya_cevir([0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert sekiz_biti_sayiya_cevir([1, 1, 1, 1, 1, 1, 1, 1]) == 255


# Gidiş-dönüş: metin -> bit -> metin aynı sonucu vermeli (Türkçe harfler dahil).
def test_gidis_donus():
    metin = "Veri iletişimi ğüşıöç"
    assert bitleri_metne_cevir(metni_bitlere_cevir(metin)) == metin


# 8'in katı olmayan bit sayısı hata vermeli.
def test_eksik_bit_hata_verir():
    with pytest.raises(ValueError):
        bitleri_metne_cevir([0, 1, 0])
