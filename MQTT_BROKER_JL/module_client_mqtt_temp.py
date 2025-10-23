import paho.mqtt.client as mqtt

# === À PERSONNALISER ===
prenom = "alex"  # à changer par le prénom de l'élève
topic_temp = f"tp/mqtt/{prenom}/temp"  # Topic pour la température

# === Callback quand un message est reçu ===
def on_message(client, userdata, message):
    print(f"Température reçue sur {message.topic} : {message.payload.decode()}")

# === Configuration client MQTT ===
client = mqtt.Client()
client.on_message = on_message  # Définir la fonction callback

client.connect("test.mosquitto.org", 1883, 60)  # Connexion au serveur MQTT

# S'abonner au topic de température
client.subscribe(topic_temp)

# === Boucle principale ===
client.loop_forever()  # Boucle infinie pour recevoir les messages