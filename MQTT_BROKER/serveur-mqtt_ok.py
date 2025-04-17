# Créé par torreszenito.juan, le 16/04/2025 en Python 3.7
import paho.mqtt.client as mqtt
import time
import random

# === À PERSONNALISER ===
prenom = "alex"  # à changer par le prénom de l'élève
topic_temp = f"tp/mqtt/{prenom}/temp"
topic_cmd = f"tp/mqtt/{prenom}/cmd"

# === Callback quand un message est reçu ===
def on_message(client, userdata, message):
    print(f"Message reçu sur {message.topic} : {message.payload.decode()}")

# === Configuration client MQTT ===
client = mqtt.Client()
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

client.subscribe(topic_cmd)

# === Boucle principale ===
while True:
    temp = round(random.uniform(90.0, 80.0), 2)
    client.publish(topic_temp, str(temp))
    print(f"Température publiée sur {topic_temp} : {temp}")

    client.loop(timeout=1.0)  # Vérifie les messages reçus
    time.sleep(5)



