# user.py
import paho.mqtt.client as mqtt_client

broker = "broker.emqx.io"
topic_prefix = "gnss/data/"

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    print("Received message:", data)

client = mqtt_client.Client('user')
client.on_message = on_message

client.connect(broker)
client.loop_start()

receiver_name = input("Enter receiver name to subscribe: ")
client.subscribe(f"{topic_prefix}{receiver_name}")

client.loop_forever()

