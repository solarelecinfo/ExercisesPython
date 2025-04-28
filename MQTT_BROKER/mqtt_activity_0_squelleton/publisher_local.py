# simulator device 1 for mqtt message publishing
import paho.mqtt.client as mqtt
import time
import random

# Paramètres de connection au Broker(serveur MQTT)
broker = "broker" # hostname
port = 0 # port mqtt
keepalive = 60 # time to live(seconds)
topic = f"topic"# topic
# client internal data
client_data="publisher:binome-raoult-pasteur"

def on_publish(client, userdata, mid):
    print(f"on_publish with userdata:{str(userdata)} and message id:{mid}")

def main():
    client = mqtt.Client(userdata=client_data)
    client.on_publish = on_publish  # callback associated function
    client.connect(broker, port, keepalive)

    #Boucle pour générer des données aléatoires de temperature===
    while True:
        temp = round(random.randint(22, 30))
        temp =str(temp)+"°C"
        client.publish(topic, temp)
        print(f"Température publiée sur {topic}:{temp}")
        time.sleep(4)

if __name__ == "__main__":
    main()



