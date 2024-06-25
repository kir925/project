# mqtt_subscriber.py
import paho.mqtt.client as mqtt_client
import time

broker = "broker.emqx.io"
topic_prefix = "gnss/data/"

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    print("Received message:", data)

client = mqtt_client.Client('subscriber')
client.on_message = on_message

client.connect(broker)
client.loop_start()

client.subscribe(f"{topic_prefix}#")

client.loop_forever()

