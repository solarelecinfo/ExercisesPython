# simple device simulator for MQTT message publishing (file-based)
import paho.mqtt.client as mqtt
import time
import uuid
from datetime import datetime

# --- paramètres de connexion au broker ---
broker = "broker"  # adresse du broker MQTT
port = 0000  # port MQTT (1883 par défaut)
keepalive = 60  # durée de vie de la session
topic = "telemetry/info_pc"  # topic MQTT
client_data = "NOM-PRENOM"  # context de session mqtt


# --- callback de publication de messages  ---
def on_publish(client, userdata, mid):
    print(f"Message publié (id={mid}) - userdata: {userdata}")

#-- Method por obtenir l'information mac et date
def get_system_info():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mac = uuid.getnode()
    msg = f"date = {str(date)} + mac = {str(mac)}"
    return msg


# --- fonction principale ---
def main():
    client = mqtt.Client(userdata=client_data)
    client.on_publish = on_publish
    client.connect(broker, port, keepalive)
    print(f"Connexion au broker MQTT {broker}:{port}")
    print(f"Publication sur le topic : {topic}")

    # boucle principale :
    while True:
        msg = get_system_info()
        client.publish(topic, msg)
        time.sleep(3)


if __name__ == "__main__":
    main()
