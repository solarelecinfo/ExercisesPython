# simple device simulator for MQTT message publishing (file-based)
import paho.mqtt.client as mqtt
import time

# --- paramètres de connexion au broker ---
broker = "localhost"      # adresse du broker MQTT
port = 1883               # port MQTT (1883 par défaut)
keepalive = 60            # durée de vie de la session
topic = "telemetry/etat"  # topic MQTT
fichier = "etat.txt"      # fichier local contenant ON ou OFF

# --- callback publication ---
def on_publish(client, userdata, mid):
    print(f"Message publié (id={mid}) - userdata: {userdata}")

# --- fonction principale ---
def main():
    client = mqtt.Client(userdata="publisher:etat_capteur")
    client.on_publish = on_publish
    client.connect(broker, port, keepalive)

    print(f"Connexion au broker MQTT {broker}:{port}")
    print(f"Lecture du fichier : {fichier}")
    print(f"Publication sur le topic : {topic}")

    # boucle principale : lit le fichier et publie la valeur toutes les 5 secondes
    while True:
        try:
            with open(fichier, "r", encoding="utf-8-sig") as f:
                etat = f.readline().strip()
        except FileNotFoundError:
            etat = "UNKNOWN"
        if etat not in ["ON", "OFF"]:

            print(f"⚠️ Valeur inattendue dans {fichier}: '{etat}' (attendu: ON ou OFF)")
        else:
            client.publish(topic, etat)
            print(f"État publié sur {topic}: {etat}")
        time.sleep(5)

if __name__ == "__main__":
    main()