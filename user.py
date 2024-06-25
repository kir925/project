# user.py
import paho.mqtt.client as mqtt_client

broker = "broker.emqx.io"
topic_prefix = "gnss/data/"

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    print("Received message:", data)

client = mqtt_client.Client('user')  # Не указываем явно протокол
client.on_message = on_message

def subscribe_to_topic(receiver_name):
    try:
        client.connect(broker)
        client.loop_start()
        client.subscribe(f"{topic_prefix}{receiver_name}")
        print(f"Subscribed to topic: {topic_prefix}{receiver_name}")
    except Exception as ex:
        print(f"Error subscribing to topic: {ex}")
        client.disconnect()

if __name__ == "__main__":
    try:
        while True:
            receiver_name = input("Enter receiver name to subscribe (or 'exit' to quit): ")
            if receiver_name.lower() == 'exit':
                break
            subscribe_to_topic(receiver_name)

        client.loop_forever()  # Цикл ожидания сообщений, обработка происходит в on_message

    except KeyboardInterrupt:
        print("Interrupted by user")
        client.disconnect()

    except mqtt_client.MQTTException as mqtt_ex:
        print(f"MQTT Exception occurred: {mqtt_ex}")
        client.disconnect()
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        client.disconnect()
