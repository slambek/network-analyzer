# Network Analyzer

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-LSTM-orange)
![Scikit-learn](https://img.shields.io/badge/ScikitLearn-RandomForest-red)
![License](https://img.shields.io/badge/License-MIT-green)

Real-time network intrusion detection system combining LSTM-based sequence analysis with Random Forest classification for anomaly detection in network traffic.

## Overview

This project explores the use of hybrid machine learning and deep learning architectures for cybersecurity and network anomaly detection. The system analyzes packet flows from PCAP traffic data and identifies suspicious or malicious network behavior in real time.

The project was developed as part of MSc Computer Science research focused on AI-driven intrusion detection systems.

## Design Goals

- Real-time intrusion detection
- Reduced false positive rate
- Temporal traffic analysis
- Explainable classification pipeline
- SOC-oriented deployment architecture

## Research Objectives

- Detect anomalous network activity using AI-based models
- Combine sequential learning with statistical classification
- Reduce false positives in intrusion detection
- Analyze packet-level network traffic in real time
- Explore hybrid ML/DL architectures for cybersecurity applications

## Features

- Hybrid detection pipeline using LSTM and Random Forest models
- Real-time traffic monitoring dashboard built with Streamlit
- Packet analysis and feature extraction using Scapy
- Network traffic simulation for testing and evaluation
- Ensemble-based anomaly scoring system
- Alerting and attack logging modules
- PCAP-based traffic processing pipeline

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

## Tech Stack

### Core
- Python
- NumPy
- Pandas

### Machine Learning
- TensorFlow / Keras
- Scikit-learn

### Networking
- Scapy

### Visualization
- Streamlit
- Matplotlib

## Dataset

The system was trained and evaluated using the UNSW-NB15 dataset, which contains modern network traffic patterns and multiple categories of malicious activity including DoS, Exploits, Reconnaissance, Shellcode, and Worms attacks.

Extracted features included:
- Packet length
- Flow duration
- Protocol type
- TCP flags
- Traffic frequency
- Source and destination statistics
- Packet timing information

## Experimental Results

| Metric | Score |
|---|---|
| Accuracy | 99.20% |
| Precision | 93.7% |
| Recall | 93.1% |
| F1 Score | 93.4% |

## Project Structure

```bash
├── .streamlit/
├── scripts/
│   ├── download_data.py
│   ├── simulate_network_traffic.py
│   └── simulate_user_behavior.py
├── src/
│   ├── models/
│   ├── accuracy_evaluation.py
│   ├── alerting.py
│   ├── attack_logging.py
│   ├── confusion_matrix_visual.py
│   ├── detection_real_time.py
│   ├── hybrid_model.py
│   └── training/
├── app.py
├── requirements.txt
└── README.md
```

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the dashboard:

```bash
streamlit run app.py
```

Run network traffic simulation:

```bash
python scripts/simulate_network_traffic.py
```

## Future Improvements

- Kafka-based traffic ingestion
- GPU-accelerated inference
- Kubernetes deployment
- SIEM integration
- Distributed packet processing
- Real-time threat intelligence feeds

## Disclaimer

This project was developed strictly for educational and research purposes.
