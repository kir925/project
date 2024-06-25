import time
import paho.mqtt.client as mqtt_client
from gnss_tec import rnx
import sys

broker = "broker.emqx.io"
topic_prefix = "gnss/data/"

def read_and_publish(file_path, receiver_name):
    print(f"File path: {file_path}")  # Добавляем отладочный вывод
    client = mqtt_client.Client(client_id=receiver_name, protocol=mqtt_client.MQTTv5)  # Используем MQTTv5
    client.connect(broker)
    client.loop_start()

    try:
        with open(file_path) as obs_file:
            reader = rnx(obs_file)
            for tec in reader:
                message = '{} {}: {} {}'.format(
                    tec.timestamp, tec.satellite, tec.phase_tec, tec.p_range_tec
                )
                client.publish(f"{topic_prefix}{receiver_name}", message)
                time.sleep(30)
    except FileNotFoundError as e:
        print(f"Error opening file: {e}")

    client.disconnect()
    client.loop_stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python receiver_service.py <receiver_name>")
        sys.exit(1)

    receiver_name = sys.argv[1]
    file_path = f"rnx_files/{receiver_name}_R_20240010000_01D_30S_MO.rnx"
    read_and_publish(file_path, receiver_name)

