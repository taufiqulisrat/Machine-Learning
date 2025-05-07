import json
import csv
import time
import os

JSON_FILE = 'cuaca_mentah_pesisir_selatan.json'
CSV_FILE = 'cuaca.csv'

def convert_json_to_csv():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Flatten jika data nested
        flattened_data = [item for sublist in data for item in sublist]

        fields = [
            "datetime", "local_datetime", "t", "tcc", "tp", "weather_desc",
            "wd", "wd_deg", "ws", "hu", "vs", "vs_text", "image"
        ]

        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for entry in flattened_data:
                writer.writerow({field: entry.get(field, '') for field in fields})

        print("✅ CSV diperbarui karena JSON berubah.")
    except Exception as e:
        print(f"❌ Gagal memperbarui CSV: {e}")

def watch_file(file_path):
    last_modified = None
    print(f"🔍 Memantau perubahan pada: {file_path}")
    while True:
        try:
            current_modified = os.path.getmtime(file_path)
            if last_modified is None or current_modified != last_modified:
                last_modified = current_modified
                convert_json_to_csv()
            time.sleep(5)  # Cek setiap 5 detik
        except FileNotFoundError:
            print("⚠️ File belum ditemukan. Menunggu...")
            time.sleep(5)

if __name__ == '__main__':
    watch_file(JSON_FILE)
