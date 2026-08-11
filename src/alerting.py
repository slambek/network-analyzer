class AlertingSystem:
    def __init__(self):
        pass  # Initialization is not required for console alerts

    def send_alert(self, packet, is_anomaly, is_threat):
        print("\n=== Alert ===")
        print("Suspicious activity detected!")
        print(f"Packet details: {packet.summary()}")

        if is_anomaly:
            print("Type: Anomalous behavior")

        if is_threat:
            print("Type: Known threat")

        print("=================\n")