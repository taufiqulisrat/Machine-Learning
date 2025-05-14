import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# === 1. Baca data ===
data = pd.read_csv('cuaca.csv', parse_dates=['local_datetime'])

# === 2. Tambah fitur waktu ===
data['hour'] = data['local_datetime'].dt.hour
data['day_of_year'] = data['local_datetime'].dt.dayofyear

# === 3. Simulasikan nilai voltage jika belum ada ===
if 'voltage' not in data.columns:
    np.random.seed(42)
    data['voltage'] = (
        0.8 * data['t'] -
        0.5 * data['hu'] +
        0.3 * data['ws'] +
        0.2 * np.random.randn(len(data)) + 20
    )

# === 4. Encode deskripsi cuaca ===
data['weather_desc'] = data['weather_desc'].astype('category')
data['weather_code'] = data['weather_desc'].cat.codes

# === 5. Pilih fitur ===
features = ['t', 'tp', 'ws', 'hu', 'hour', 'day_of_year', 'weather_code']
X = data[features]
y = data['voltage']

# === 6. Split data ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === 7. Latih model ===
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# === 8. Evaluasi ===
y_pred = model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.3f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.3f}")

# === 9. Prediksi dan Simpan Hasil ===
data['predicted_voltage'] = model.predict(X)  # Prediksi tegangan berdasarkan data asli
data.to_csv('hasil_prediksi_tegangan.csv', index=False)  # Simpan hasil prediksi ke CSV

print("✅ Prediksi disimpan ke hasil_prediksi_tegangan.csv")
