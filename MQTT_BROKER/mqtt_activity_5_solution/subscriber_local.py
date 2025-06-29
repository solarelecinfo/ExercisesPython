import threading
import paho.mqtt.client as mqtt
import time
import random
import tkinter as tk
import tkinter.scrolledtext as scrolledtext

# Main layout definition
main_layout = tk.Tk()
main_layout.title("MQTT Temperature Subscriber")
main_layout.geometry("650x500")  # taille en pixel de l'écran
log_box = None


# Paramètres de connection au Broker(serveur MQTT)
broker = tk.StringVar(value = "127.0.0.1")  # tkinder input variable "localhost"
port = tk.IntVar(value = 1883)  # tkinder input variable port mqtt
keepalive = 60  # time to live(seconds)
topic = tk.StringVar(value="telemetry/temp")  # topic
client_data = tk.StringVar(value = "subscriber:nom1-nom2")

#fonction pour logger via un UI box
def log_message(msg):
    # Utiliser after() pour mettre à jour l'interface depuis le thread principal
    main_layout.after(0, lambda: log_box.insert(tk.END, msg + "\n"))
    main_layout.after(0, lambda: log_box.see(tk.END))

def on_message(client, userdata, msg):
    payload=msg.payload.decode()
    log_message(f"on_message with userdata:{str(userdata)} and payload:{payload}")

def config_ui_interface():
    # Définition de champs
    broker_host = tk.Label(main_layout, text="Broker:")
    broker_host_entry = tk.Entry(main_layout, textvariable=broker)

    broker_port = tk.Label(main_layout, text="Port:")
    broker_port_entry = tk.Entry(main_layout, textvariable=port)

    broker_topic = tk.Label(main_layout, text="Topic:")
    broker_topic_entry = tk.Entry(main_layout, textvariable=topic)

    broker_client_data = tk.Label(main_layout, text="Client_data:")
    broker_client_data_entry = tk.Entry(main_layout, textvariable=client_data)

    # Placement de champs dans le main_layout en mode FIFO
    broker_host.pack()
    broker_host_entry.pack()

    broker_port.pack()
    broker_port_entry.pack()

    broker_topic.pack()
    broker_topic_entry.pack()

    broker_client_data.pack()
    broker_client_data_entry.pack()

    # Bouton pour récupérer les valeurs et afficher dans la console
    submit_button = tk.Button(main_layout, text="Valider", command=submit_server_values)
    submit_button.pack()

    # Zone de text pour logs
    global log_box #reference variable global
    log_box = scrolledtext.ScrolledText(main_layout, width=65, height=20)
    log_box.pack()

    # Lancer l'interface Tkinter
    main_layout.mainloop()

def submit_server_values():
    print("Broker:", broker.get())  # Récupère la valeur de broker
    print("Port:", port.get())  # Récupère la valeur de port
    print("keepalive:", keepalive)
    print("topic:", topic)
    print("client_data:", client_data.get())

    # lance un serveur
    threading.Thread(target=subscribe_start_button, daemon=True).start()

def subscribe_start_button():
    client = mqtt.Client(userdata=client_data.get())
    client.on_message = on_message  #callback associated function
    client.connect(broker.get(), port.get(), keepalive)
    client.subscribe(topic.get())
    client.loop_forever()

def main():
    config_ui_interface()

if __name__ == "__main__":
    main()
