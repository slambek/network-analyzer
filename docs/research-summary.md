# Research Summary

This study investigates a hybrid approach to network intrusion detection based on sequential and ensemble machine learning methods.

The proposed system combines an LSTM network for modelling temporal patterns in network traffic with a Random Forest classifier for traffic classification and anomaly detection. The approach is intended to capture both sequential dependencies and non-linear relationships in extracted traffic features.

The experimental evaluation was conducted using the UNSW-NB15 dataset. The system achieved an accuracy of **99.20%**, with a precision of **93.7%**, recall of **93.1%**, and F1-score of **93.4%**.

The implementation covers network traffic parsing, feature extraction, model inference, anomaly scoring, and real-time visualization through a Streamlit interface.

The results provide an experimental evaluation of the proposed hybrid approach for network intrusion detection.
