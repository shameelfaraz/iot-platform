import json
import time
import random
import paho.mqtt.client as mqtt
from datetime import datetime

client = mqtt.Client()
client.connect("mqtt", 1883, 60)

while True:
    payload = {
        "sensor_id": "sim_livingroom_1",
        "temperature": round(random.uniform(18, 25), 2),
        "humidity": round(random.uniform(35, 60), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

    client.publish("home/livingroom/sensor", json.dumps(payload))
    print("Published:", payload)
    time.sleep(5)
