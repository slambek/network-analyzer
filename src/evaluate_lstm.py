import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model and scaler
model = tf.keras.models.load_model("lstm_model.h5")
scaler_mean = np.load("scaler_lstm.npy")

# Load test data
data = pd.read_csv("../data/processed/train_processed.csv")

features = ['duration', 'src_bytes', 'dst_bytes', 'wrong_fragment']
X_test = data[features].values
y_test = data['binary_label'].values

# Normalize the input features
X_test = (X_test - scaler_mean) / np.std(X_test, axis=0)

# Reshape data for LSTM input
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

# Generate predictions
y_pred_probs = model.predict(X_test)
y_pred = (y_pred_probs > 0.5).astype(int).flatten()

# Display evaluation metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Plot the confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(
    confusion_matrix(y_test, y_pred),
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Normal', 'Attack'],
    yticklabels=['Normal', 'Attack']
)

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('LSTM Confusion Matrix')
plt.show()