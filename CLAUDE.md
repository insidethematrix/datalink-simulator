# Proje: Veri Bağı Katmanı Simülatörü
Veri iletişimi dersi projesi. Python + Streamlit. Teslim süresi 20 gün.

## Amaç
Kullanıcının girdiği mesajı bitlere çevirip gürültülü bir kanaldan geçiren,
hata kontrolü (Parity, CRC) yapan ve ARQ protokolleriyle
(Stop-and-Wait, Go-Back-N) iletimi simüle eden bir uygulama.

## Kurallar
- Ben bu konuları yeni öğreniyorum. Her kodu yazdıktan sonra ne yaptığını
  Türkçe ve basitçe, örnekle açıkla.
- Kod sade ve okunabilir olsun. İleri seviye Python hileleri kullanma.
- Her fonksiyona Türkçe yorum satırı ekle.
- Her modül için pytest ile basit testler yaz.
- Bir seferde sadece istediğim kısmı yap, sonraki adımlara geçme.
- Grafiklerde Plotly kullan.

## Modüller
encoding.py      -> metin <-> bit dönüşümü
channel.py       -> gürültülü kanal
error_control.py -> parity ve CRC
arq.py           -> Stop-and-Wait ve Go-Back-N
app.py           -> Streamlit arayüzü
tests/           -> testler

## Yol haritası ve kurulum
Ayrıntılar için README.md dosyasına bak.

## Durum
- [x] Kurulum (.venv, requirements.txt, .gitignore)
- [x] encoding.py: text_to_bits, byte_to_int, bits_to_text + testler
- [x] channel.py: transmit(bits, error_rate, seed), find_error_positions + testler
- [x] error_control.py: compute_parity_bit/add_parity/check_parity ("even"/"odd"),
      crc_remainder/add_crc/check_crc (CRC8_POLY varsayılan, CRC3_POLY elle örnek) + testler
- [ ] arq.py (sıradaki adım)
- [ ] app.py
- GitHub: https://github.com/insidethematrix/datalink-simulator (main dalı)

## Çalışma şekli
- Bitler 0/1 tamsayı listesi olarak tutulur (ör. [0, 1, 0, 0, 0, 0, 0, 1]).
- Kod adları (fonksiyon, değişken, test adları) İngilizce; yorumlar ve
  kullanıcıya görünen mesajlar (hata mesajları, arayüz metinleri) Türkçe.
- Her modülde kilit kısmı (2-10 satır) TODO(human) olarak ben yazıyorum;
  sen iskeleti hazırlayıp, kodumu kontrol edip açıklıyorsun.
- Testleri benim kodum bittikten sonra yaz, önce değil.
- Testler: `.venv\Scripts\python.exe -m pytest -v`
