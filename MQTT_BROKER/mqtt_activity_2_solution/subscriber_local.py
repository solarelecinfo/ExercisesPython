import paho.mqtt.client as mqtt

# Paramètres de connection au Broker(serveur MQTT)
broker = "localhost" # hostname
port = 1883 # port mqtt
keepalive = 60 # keep alive time(seconds)
topic = f"telemetry/temp"# topic

# client internal data
client_data="subscriber:raoult-pasteur"

def on_message(client, userdata, msg):
    client_id=client._client_id.decode()
    payload=msg.payload.decode()
    print(f"on_message with userdata:{str(userdata)} and id:{client_id} payload:{payload}")

def main():
    client = mqtt.Client(userdata=client_data)
    client.on_message = on_message #callback associated function
    client.connect(broker, port, keepalive)
    client.subscribe(topic)
    client.loop_forever()

if __name__ == "__main__":
    main()
