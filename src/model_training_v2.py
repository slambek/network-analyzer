from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("../data/processed/train_processed.csv")

features = ['duration', 'src_bytes', 'dst_bytes', 'wrong_fragment']
X = data[features]
y = data['binary_label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

rf_model = RandomForestClassifier(
    n_estimators=50,
    max_depth=10,
    random_state=42
)

rf_model.fit(X_train, y_train)

joblib.dump(rf_model, "rf_model_fixed.pkl")

print("Random Forest model saved successfully.")