import paho.mqtt.client as mqtt

# Paramètres de connection au Broker(serveur MQTT)
broker = "broker" # hostname
port = 0000 # port mqtt
keepalive = 60 # keep alive time(seconds)
topic = "telemetry/info_pc"# topic

# client internal data
client_data = "NOM-PRENOM"

def on_message( client,userdata, msg):
    payload=msg.payload.decode()
    print(f"on_message with userdata:{str(userdata)} and payload:{payload}")

def main():
    client = mqtt.Client(userdata=client_data)
    client.on_message = on_message #callback associated function
    client.connect(broker, port, keepalive)
    client.subscribe(topic)
    client.loop_forever()

if __name__ == "__main__":
    main()
