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
