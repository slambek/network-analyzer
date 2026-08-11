# System Architecture

## Detection Pipeline

```text
Network Traffic
       ↓
Packet Capture & Parsing
       ↓
Feature Extraction
       ↓
 ┌──────────────┐
 │ LSTM Network │
 └──────────────┘
         +
 ┌──────────────┐
 │ Random Forest│
 └──────────────┘
       ↓
 Hybrid Ensemble
       ↓
 Anomaly Detection
       ↓
 Alerting
       ↓
 Streamlit Dashboard
```

## Components

**Traffic Processing**
Packet parsing, protocol analysis, and feature extraction from network traffic.

**LSTM**
Models temporal dependencies in sequential traffic patterns.

**Random Forest**
Classifies traffic based on extracted statistical features.

**Hybrid Ensemble**
Combines predictions from both models for anomaly classification.

**Dashboard**
Provides real-time visualization of traffic, anomalies, and alerts.
