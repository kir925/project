import paho.mqtt.client as mqtt_client

broker = "broker.emqx.io"
topic_prefix = "gnss/data/"

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    print("Received message:", data)

client = mqtt_client.Client('user')  # Не указываем явно протокол
client.on_message = on_message

try:
    client.connect(broker)
    client.loop_start()

    receiver_name = input("Enter receiver name to subscribe: ")
    client.subscribe(f"{topic_prefix}{receiver_name}")

    while True:
        pass  # Цикл ожидания сообщений, обработка происходит в on_message

except KeyboardInterrupt:
    print("Interrupted by user")
    client.disconnect()

except mqtt_client.MQTTException as mqtt_ex:
    print(f"MQTT Exception occurred: {mqtt_ex}")
    client.disconnect()

except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
    client.disconnect()

