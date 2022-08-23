import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("message topic:\t", message.topic)
    print(f"message fact:\t {str(message.payload.decode('utf-8'))}")
    print("-"*50)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # client.subscribe("topic/#")       # subscribe to all topics
    client.subscribe("topic/cats")      # subscribe to cats topics
    client.subscribe("topic/apes")      # subscribe to apes topics


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))
    print("Program Terminated")


broker = "test.mosquitto.org"
client = mqtt.Client("Animal_Subscriber_Smartphone")
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect(broker)
client.loop_start()
time.sleep(20)
client.loop_stop()
client.disconnect()
