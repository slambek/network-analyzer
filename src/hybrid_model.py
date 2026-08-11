import numpy as np
import pandas as pd
import joblib
import tensorflow as tf

# Load the trained models
rf_model = joblib.load("rf_model_fixed.pkl")
lstm_model = tf.keras.models.load_model("lstm_model.h5")
scaler_mean = np.load("scaler_lstm.npy")

# Simulated network traffic
new_data = pd.DataFrame({
    'duration': [5],
    'src_bytes': [1000],
    'dst_bytes': [2000],
    'wrong_fragment': [0]
})

# Generate Random Forest prediction
rf_pred = rf_model.predict(new_data)

# Generate LSTM prediction
X_new = (new_data.values - scaler_mean) / np.std(
    new_data.values,
    axis=0
)

X_new = X_new.reshape(
    (X_new.shape[0], 1, X_new.shape[1])
)

lstm_pred = lstm_model.predict(X_new)

# Combine model predictions
final_prediction = (
    rf_pred + (lstm_pred > 0.5).astype(int)
) // 2

# Display the result
if final_prediction[0] == 1:
    print("Warning: Potential attack detected!")
else:
    print("Traffic is normal.")