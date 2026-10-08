# Veri Bağı Katmanı Simülatörü

Kullanıcının girdiği mesajı bitlere çevirip gürültülü bir kanaldan geçiren,
hata kontrolü (Parity, CRC) yapan ve ARQ protokolleriyle
(Stop-and-Wait, Go-Back-N) iletimi simüle eden bir Streamlit uygulaması.

## Kurulum (Windows / PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Çalıştırma

```powershell
pytest                 # testleri çalıştırır
streamlit run app.py   # arayüzü açar
```

## Modüller

| Dosya | Görevi |
|-------|--------|
| `encoding.py` | Metin <-> bit dönüşümü |
| `channel.py` | Gürültülü kanal (bitleri rastgele bozar) |
| `error_control.py` | Parity ve CRC ile hata tespiti |
| `arq.py` | Stop-and-Wait ve Go-Back-N protokolleri |
| `app.py` | Streamlit arayüzü (Plotly grafikleri) |
| `tests/` | pytest testleri |

## Yol Haritası (20 gün)

| Gün | Adım | Çıktı |
|-----|------|-------|
| 1 | Kurulum | venv, requirements, iskelet |
| 2–3 | `encoding.py` | Metni bitlere, bitleri metne çevirme + testler |
| 4–5 | `channel.py` | Bit hata olasılığı (BER) ile rastgele bit çevirme, `seed` desteği + testler |
| 6–8 | `error_control.py` | Çift/tek parity, CRC (polinom bölmesi) ekleme/kontrol + testler |
| 9–12 | `arq.py` | Stop-and-Wait, Go-Back-N (pencere, zaman aşımı, yeniden iletim) + testler |
| 13–16 | `app.py` | Mesaj girişi, BER ayarı, yöntem seçimi, Plotly grafikleri |
| 17–18 | Entegrasyon | Uçtan uca deneme, hata düzeltmeleri |
| 19–20 | Teslim | README, ekran görüntüleri, rapor/sunum |

Bağımlılık sırası: `encoding` → `channel` → `error_control` → `arq` → `app`
