# channel.py modülünün testleri.
import pytest

from channel import kanaldan_gecir, hatali_konumlari_bul


# Hata olasılığı 0 ise hiçbir bit değişmemeli.
def test_hatasiz_kanal():
    assert kanaldan_gecir([0, 1, 0, 1], 0.0) == [0, 1, 0, 1]


# Hata olasılığı 1 ise bütün bitler ters dönmeli.
def test_tamamen_bozuk_kanal():
    assert kanaldan_gecir([0, 1, 0, 1], 1.0) == [1, 0, 1, 0]


# Aynı seed her seferinde aynı sonucu vermeli.
def test_ayni_seed_ayni_sonuc():
    bitler = [0, 1] * 50
    assert kanaldan_gecir(bitler, 0.3, seed=42) == kanaldan_gecir(bitler, 0.3, seed=42)


# 10000 bitte, 0.1 olasılıkla yaklaşık 1000 hata çıkmalı.
def test_hata_orani_yaklasik_dogru():
    bitler = [0] * 10000
    alinan = kanaldan_gecir(bitler, 0.1, seed=1)
    hata_sayisi = len(hatali_konumlari_bul(bitler, alinan))
    assert 800 < hata_sayisi < 1200


# Geçersiz olasılık hata vermeli.
def test_gecersiz_olasilik():
    with pytest.raises(ValueError):
        kanaldan_gecir([0, 1], 1.5)


# Farklı bitlerin konumları doğru bulunmalı.
def test_hatali_konumlar():
    assert hatali_konumlari_bul([0, 1, 0, 1], [0, 0, 0, 0]) == [1, 3]
