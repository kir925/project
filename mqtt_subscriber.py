
import paho.mqtt.client as mqtt_client
from paho.mqtt.client import MQTTv31

def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.to>

client = mqtt_client.Client(client_id='subscriber', clean_session=True, userdat>
client.on_message = on_message

broker_address = "broker.emqx.io"
print(f"Connecting to MQTT broker at {broker_address}")
client.connect(broker_address)

print("Subscribing to topic 'lab/leds/state'")
client.subscribe("lab/leds/state")

client.loop_forever()

