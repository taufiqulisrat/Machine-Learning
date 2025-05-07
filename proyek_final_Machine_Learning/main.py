import subprocess
import os

# Ganti dengan path ke folder tempat semua script berada
BASE_DIR = "E:/SEMESTER 6/mesin learning/UAS_ML"

# Daftar script yang akan dijalankan dalam urutan
scripts = [
    "ambil_cuaca_bmkg.py",
    "convert_json_to_csv.py",
    "prediksi_tegangan.py"
]

def jalankan_script(script_name):
    full_path = os.path.join(BASE_DIR, script_name)
    
    if not os.path.exists(full_path):
        print(f"[❌ ERROR] File tidak ditemukan: {full_path}")
        return False

    try:
        print(f"\n▶️ Menjalankan {script_name}...")
        result = subprocess.run(
            ["python", full_path],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8"  # Memastikan output terbaca dengan benar
        )
        print(f"[✅ BERHASIL] {script_name} selesai.\n📄 Output:\n{result.stdout}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"[❌ GAGAL] {script_name} gagal dijalankan.")
        print(f"🔧 Error:\n{e.stderr}")
        return False

def main():
    semua_berhasil = True

    for script in scripts:
        berhasil = jalankan_script(script)
        if not berhasil:
            semua_berhasil = False
            print("\n🛑 Proses dihentikan karena terjadi error.")
            break

    if semua_berhasil:
        print("\n🎉 Semua script berhasil dijalankan tanpa error.")
    else:
        print("\n⚠️ Beberapa script gagal. Silakan periksa error di atas.")

if __name__ == "__main__":
    main()
