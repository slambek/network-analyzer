import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score, accuracy_score, precision_score, recall_score, f1_score
import plotly.graph_objects as go
import plotly.figure_factory as ff
from st_aggrid import AgGrid, GridOptionsBuilder
import os

os.environ["STREAMLIT_SERVER_MAX_UPLOAD_SIZE"] = "1024"

pd.set_option("styler.render.max_elements", 3000000)
st.set_page_config(layout="wide")

@st.cache_resource
def load_models():
    rf_model = joblib.load("src/rf_model_fixed.pkl")
    lstm_model = tf.keras.models.load_model("src/lstm_model.h5")
    scaler_mean = np.load("src/scaler_lstm.npy")
    return rf_model, lstm_model, scaler_mean

rf_model, lstm_model, scaler_mean = load_models()

st.title("Network Analyzer")
uploaded_file = st.file_uploader("Upload traffic data", type=["csv", "xlsx", "parquet"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        data = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith(".parquet"):
        data = pd.read_parquet(uploaded_file)
    else:
        st.error("Unsupported file format")
        st.stop()

    st.subheader("Preview Data")
    st.dataframe(data.head())

    required_columns = ['duration', 'src_bytes', 'dst_bytes', 'wrong_fragment']
    if not all(col in data.columns for col in required_columns):
        st.error(f"The file must contain columns: {', '.join(required_columns)}")
        st.stop()

    X = data[required_columns].values
    if len(required_columns) != scaler_mean.shape[0]:
        st.error("The number of features does not match the trained model")
        st.stop()

    X_norm = (X - scaler_mean) / np.std(X, axis=0)
    X_lstm = X_norm.reshape((X_norm.shape[0], 1, X_norm.shape[1]))

    rf_preds = rf_model.predict(X)
    lstm_preds = (lstm_model.predict(X_lstm) > 0.5).astype(int).flatten()
    hybrid_preds = (rf_preds + lstm_preds) // 2

    results_df = data.copy()
    results_df['RF'] = rf_preds
    results_df['LSTM'] = lstm_preds
    results_df['Hybrid'] = hybrid_preds
    results_df['Status'] = results_df['Hybrid'].map({0: 'Normal', 1: 'Attack'})

    tab1, tab2 = st.tabs(["Results", "Model Metrics"])

    with tab1:
        st.subheader(f"Analysis Results · {len(results_df)} records")
        gb = GridOptionsBuilder.from_dataframe(results_df)
        gb.configure_pagination()
        gb.configure_default_column(filter=True, resizable=True, sortable=True)
        AgGrid(results_df, gridOptions=gb.build())

        st.subheader("Summary")
        col1, col2 = st.columns(2)
        col1.metric("Attacks", int(hybrid_preds.sum()))
        col2.metric("Normal", int((hybrid_preds == 0).sum()))
        st.bar_chart(results_df['Hybrid'].value_counts())

        csv = results_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results", csv, "prediction_result.csv", "text/csv")

    with tab2:
        st.subheader("Classification Metrics")

        if 'binary_label' in data.columns:
            y_true = data['binary_label'].values

            def plot_roc_interactive(fpr, tpr, auc, model_name):
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f"AUC = {auc:.2f}"))
                fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], line=dict(dash='dash'), name='baseline'))
                fig.update_layout(
                    title=f"ROC Curve: {model_name}",
                    xaxis_title="FPR",
                    yaxis_title="TPR"
                )
                st.plotly_chart(fig)

            def plot_confusion_matrix_interactive(cm, labels, model_name):
                z = cm.tolist()
                fig = ff.create_annotated_heatmap(
                    z, x=labels, y=labels, colorscale='Blues', showscale=True,
                    annotation_text=[[str(val) for val in row] for row in z], font_colors=["black"]
                )
                fig.update_layout(
                    title=f"Confusion Matrix: {model_name}",
                    xaxis_title="Prediction",
                    yaxis_title="Actual"
                )
                st.plotly_chart(fig, use_container_width=True)

            def show_metrics(y_true, y_pred, model_name):
                st.markdown(f"### {model_name}")
                df_report = pd.DataFrame(classification_report(y_true, y_pred, output_dict=True)).transpose()
                st.dataframe(df_report)

                cm = confusion_matrix(y_true, y_pred)
                plot_confusion_matrix_interactive(cm, ["Normal", "Attack"], model_name)

                fpr, tpr, _ = roc_curve(y_true, y_pred)
                auc = roc_auc_score(y_true, y_pred)
                plot_roc_interactive(fpr, tpr, auc, model_name)

            show_metrics(y_true, rf_preds, "Random Forest")
            show_metrics(y_true, lstm_preds, "LSTM")
            show_metrics(y_true, hybrid_preds, "Hybrid")

            st.subheader("Model Comparison")
            models = {
                "Random Forest": rf_preds,
                "LSTM": lstm_preds,
                "Hybrid": hybrid_preds
            }
            comparison_data = []
            for name, y_pred in models.items():
                comparison_data.append({
                    "Model": name,
                    "Accuracy": accuracy_score(y_true, y_pred),
                    "Precision": precision_score(y_true, y_pred, zero_division=0),
                    "Recall": recall_score(y_true, y_pred, zero_division=0),
                    "F1": f1_score(y_true, y_pred, zero_division=0),
                    "AUC": roc_auc_score(y_true, y_pred)
                })
            df_comparison = pd.DataFrame(comparison_data).set_index("Model")
            st.dataframe(df_comparison.style.highlight_max(axis=0, color='lightgreen'))

        else:
            st.warning(
                "The file does not contain `binary_label`. Metrics are unavailable."
            )
else:
    st.info("Upload a file to start the analysis.")