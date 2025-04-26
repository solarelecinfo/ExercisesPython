# simulator device 1 for mqtt message publishing
import paho.mqtt.client as mqtt
import time
import random

# Paramètres de connection au Broker(serveur MQTT)
broker = "localhost" # hostname
port = 1883 # port mqtt
keepalive = 60 # time to live(seconds)
topic = f"telemetry/temp"# topic
# client internal data
client_data="publisher-binome:raoult-pasteur"

def on_publish(client, userdata, mid):
    client_id=client._client_id.decode()
    print(f"on_publish with userdata:{str(userdata)} and id:{client_id} et message id:{mid}")

def main():
    client = mqtt.Client(userdata=client_data)
    client.on_publish = on_publish  # callback associated function
    client.connect(broker, port, keepalive)

    # === Boucle pour generer des données alèatoires de temperature===
    while True:
        temp = round(random.randint(20, 30))
        client.publish(topic, str(temp))
        print(f"Température publiée sur {topic}:{temp}°C")
        time.sleep(4)

if __name__ == "__main__":
    main()



