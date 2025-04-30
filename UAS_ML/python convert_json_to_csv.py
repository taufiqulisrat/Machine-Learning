import json
import csv

# Baca file JSON (gantilah 'cuaca.json' dengan nama file kamu jika beda)
with open('cuaca_mentah_pesisir_selatan.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Flatten semua entri ke satu list
flattened_data = [item for sublist in data for item in sublist]

# Tentukan field yang ingin diekspor ke CSV
fields = [
    "datetime", "local_datetime", "t", "tcc", "tp", "weather_desc",
    "wd", "wd_deg", "ws", "hu", "vs", "vs_text", "image"
]

# Tulis ke file CSV
with open('cuaca.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for entry in flattened_data:
        writer.writerow({field: entry.get(field, '') for field in fields})

print("✅ File CSV berhasil dibuat: cuaca.csv")
