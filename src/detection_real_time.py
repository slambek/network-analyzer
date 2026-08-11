import pandas as pd
import joblib

# Load the trained model
rf_model = joblib.load("rf_model_fixed.pkl")

# Simulated incoming network data
new_data = pd.DataFrame({
    'duration': [5],
    'src_bytes': [1000],
    'dst_bytes': [2000],
    'wrong_fragment': [0]
})

# Generate prediction
prediction = rf_model.predict(new_data)

# Display the result
if prediction[0] == 1:
    print("Warning: Potential attack detected!")
else:
    print("Traffic is normal.")