import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# === 1. Baca data cuaca ===
file_path = 'cuaca.csv'  # Ganti sesuai lokasi file kamu
data = pd.read_csv(file_path)

# === 2. Pra-proses data ===
# Pilih fitur penting
features = ['t', 'tp', 'ws', 'hu']  # suhu, tekanan, kecepatan angin, kelembaban

# Simulasikan target 'voltage' (tegangan)
np.random.seed(42)
data['voltage'] = (
    0.8 * data['t'] -
    0.5 * data['hu'] +
    0.3 * data['ws'] +
    0.2 * np.random.randn(len(data)) + 20
)

# Pisahkan fitur dan target
X = data[features]
y = data['voltage']

# === 3. Split data ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === 4. Latih model ===
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# === 5. Evaluasi model ===
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# === 6. Prediksi dengan data baru (data asli tanpa voltage) ===
new_data = data[features]
data['predicted_voltage'] = model.predict(new_data)

# === 7. Simpan hasil prediksi ke CSV ===
data.to_csv('hasil_prediksi_tegangan.csv', index=False)
print("Prediksi disimpan ke hasil_prediksi_tegangan.csv")
