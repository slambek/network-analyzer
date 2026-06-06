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
 │ RandomForest │
 └──────────────┘
       ↓
 Hybrid Ensemble
       ↓
 Anomaly Detection
       ↓
 Alerting System
       ↓
 Streamlit Dashboard
```

## Core Components

### Traffic Processing

Responsible for packet parsing, protocol analysis, and traffic feature extraction from PCAP data.

### LSTM Model

Processes sequential traffic behavior and temporal packet patterns.

### Random Forest Model

Performs statistical classification using extracted traffic features.

### Hybrid Ensemble

Combines outputs from both models to improve detection stability and reduce false positives.

### Monitoring Dashboard

Provides real-time traffic visualization, anomaly monitoring, and alerting through Streamlit.
