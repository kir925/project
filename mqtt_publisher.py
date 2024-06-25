# mqtt_publisher.py
import paho.mqtt.client as mqtt_client

broker = "broker.emqx.io"
topic_prefix = "gnss/data/"
client = mqtt_client.Client(client_id='publisher', clean_session=True, userdata>

client.connect(broker)
client.loop_start()

# Никаких дополнительных действий, просто оставляем клиента подключенным
client.loop_forever()
