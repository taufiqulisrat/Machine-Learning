import requests
import json
import sys

# Konfigurasi
adm4_code = "13.01.05.2003"  # Kode wilayah Pesisir Selatan
url = f"https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={adm4_code}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Ambil data dari BMKG
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print(f"❌ Gagal mengambil data dari BMKG: {e}")
    sys.exit(1)

# Cek dan ekstrak semua entry cuaca
raw_entries = []
if 'data' in data:
    for lokasi in data['data']:
        if 'cuaca' in lokasi and isinstance(lokasi['cuaca'], list):
            raw_entries.extend(lokasi['cuaca'])

# Simpan data mentah ke file
if raw_entries:
    try:
        with open("cuaca_mentah_pesisir_selatan.json", "w", encoding="utf-8") as f:
            json.dump(raw_entries, f, indent=2)
        print("✅ Data mentah berhasil disimpan ke 'cuaca_mentah_pesisir_selatan.json'.")
    except Exception as e:
        print(f"❌ Gagal menyimpan data: {e}")
else:
    print("❌ Tidak ada entri cuaca ditemukan.")
