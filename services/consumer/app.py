import json
import time
import psycopg2
import paho.mqtt.client as mqtt



def connect_db():
    while True:
        try:
            return psycopg2.connect(
                host="postgres",
                dbname="iot",
                user="iot",
                password="iot"
            )
        except psycopg2.OperationalError:
            print("Waiting for Postgres...")
            time.sleep(3)


conn = connect_db()
cur = conn.cursor()

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    cur.execute(
        """
        INSERT INTO sensor_readings(sensor_id, temperature, humidity, timestamp)
        VALUES (%s, %s, %s, %s)
        """,
        (
            data["sensor_id"],
            data["temperature"],
            data["humidity"],
            data["timestamp"],
        )
    )
    conn.commit()
    print("Inserted:", data)

client = mqtt.Client()
client.connect("mqtt", 1883, 60)
client.subscribe("home/livingroom/sensor")
client.on_message = on_message

client.loop_forever()
