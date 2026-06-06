# Hybrid AI Intrusion Detection System

Real-time network intrusion detection system combining LSTM-based sequence analysis with Random Forest classification for anomaly detection in network traffic.

## Overview

This project explores the use of hybrid AI architectures for cybersecurity and network anomaly detection. The system combines deep learning and traditional machine learning techniques to analyze packet flows and identify suspicious behavior from PCAP traffic data.

## Features

- Hybrid detection pipeline using LSTM and Random Forest models
- Real-time traffic monitoring dashboard built with Streamlit
- Packet analysis and feature extraction with Scapy
- Network traffic simulation for testing and evaluation
- Ensemble-based anomaly scoring system

## Tech Stack

- Python
- TensorFlow / Keras
- Scikit-learn
- Scapy
- Pandas / NumPy
- Streamlit

## Architecture

- **LSTM Model** — sequential traffic pattern analysis
- **Random Forest** — statistical packet classification
- **Hybrid Ensemble** — combined anomaly scoring logic
- **Streamlit Dashboard** — real-time visualization layer

## Project Structure

```bash
├── .streamlit/
├── scripts/
├── src/
│   ├── models/
│   ├── hybrid_model.py
│   ├── detection_real_time.py
│   └── training/
├── app.py
└── requirements.txt
```

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start dashboard:

```bash
streamlit run app.py
```

Run traffic simulation:

```bash
python scripts/simulate_network_traffic.py
```

## Research Focus

- Intrusion Detection Systems (IDS)
- AI-driven cybersecurity
- Network anomaly detection
- Hybrid ML/DL architectures
- Real-time packet analysis

## Disclaimer

This project was developed for educational and research purposes.
