# channel.py modülünün testleri.
import pytest

from channel import transmit, find_error_positions


# Hata olasılığı 0 ise hiçbir bit değişmemeli.
def test_noiseless_channel():
    assert transmit([0, 1, 0, 1], 0.0) == [0, 1, 0, 1]


# Hata olasılığı 1 ise bütün bitler ters dönmeli.
def test_fully_noisy_channel():
    assert transmit([0, 1, 0, 1], 1.0) == [1, 0, 1, 0]


# Aynı seed her seferinde aynı sonucu vermeli.
def test_same_seed_same_result():
    bits = [0, 1] * 50
    assert transmit(bits, 0.3, seed=42) == transmit(bits, 0.3, seed=42)


# 10000 bitte, 0.1 olasılıkla yaklaşık 1000 hata çıkmalı.
def test_error_rate_approximately_correct():
    bits = [0] * 10000
    received = transmit(bits, 0.1, seed=1)
    error_count = len(find_error_positions(bits, received))
    assert 800 < error_count < 1200


# Geçersiz olasılık hata vermeli.
def test_invalid_error_rate():
    with pytest.raises(ValueError):
        transmit([0, 1], 1.5)


# Farklı bitlerin konumları doğru bulunmalı.
def test_find_error_positions():
    assert find_error_positions([0, 1, 0, 1], [0, 0, 0, 0]) == [1, 3]
