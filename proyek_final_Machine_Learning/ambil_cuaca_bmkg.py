import requests
import json
import sys
import os
from datetime import datetime

adm4_code = "13.01.05.2003"  # IV Jurai
url = f"https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={adm4_code}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def sudah_diperbarui_hari_ini(file_path="last_update.txt"):
    if not os.path.exists(file_path):
        return False
    with open(file_path, "r") as f:
        last_date = f.read().strip()
    return last_date == datetime.today().strftime("%Y-%m-%d")

def perbarui_tanggal_hari_ini(file_path="last_update.txt"):
    with open(file_path, "w") as f:
        f.write(datetime.today().strftime("%Y-%m-%d"))

if sudah_diperbarui_hari_ini():
    print("ℹ️ Data sudah diperbarui hari ini. Tidak mengambil ulang.")
    sys.exit(0)

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print(f"❌ Gagal mengambil data dari BMKG: {e}")
    sys.exit(1)

raw_entries = []
if 'data' in data:
    for lokasi in data['data']:
        if 'cuaca' in lokasi and isinstance(lokasi['cuaca'], list):
            raw_entries.extend(lokasi['cuaca'])

if raw_entries:
    try:
        with open("cuaca_mentah_pesisir_selatan.json", "w", encoding="utf-8") as f:
            json.dump(raw_entries, f, indent=2, ensure_ascii=False)
        perbarui_tanggal_hari_ini()
        print("✅ Data mentah berhasil disimpan ke 'cuaca_mentah_pesisir_selatan.json'.")
    except Exception as e:
        print(f"❌ Gagal menyimpan data: {e}")
else:
    print("❌ Tidak ada entri cuaca ditemukan.")
