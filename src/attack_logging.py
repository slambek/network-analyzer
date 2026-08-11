import pandas as pd
import joblib

# Load the trained model
rf_model = joblib.load("rf_model_fixed.pkl")

# Log file
log_file = "attack_logs.txt"

# Simulated network traffic
new_data = pd.DataFrame({
    'duration': [2, 30, 200],
    'src_bytes': [200, 10000, 50000],
    'dst_bytes': [5000, 3000, 7000],
    'wrong_fragment': [0, 1, 0]
})

# Generate predictions
predictions = rf_model.predict(new_data)

# Write predictions to the log file
with open(log_file, "a", encoding="utf-8") as log:
    for i, pred in enumerate(predictions):
        if pred == 1:
            log.write(f"Attack detected! Record {i}\n")
        else:
            log.write(f"Normal traffic: record {i}\n")

print(f"Attack log saved to {log_file}")