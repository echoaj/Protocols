import paho.mqtt.client as mqtt
import time
import random
import json


with open('animals.json') as file:
    data = json.load(file)
    animals = list(data.keys())


# Public test broker.
broker = "mqtt.eclipseprojects.io"      # Can also use "test.mosquitto.org"
client = mqtt.Client("Animal_Publisher_Magazine")
client.connect(broker)


while True:
    animal = random.choice(animals)
    fact = random.choice(data[animal])
    topic = "topic/" + animal
    client.publish(topic, fact)
    print(f"published {animal} fact to {topic}")
    time.sleep(2)
