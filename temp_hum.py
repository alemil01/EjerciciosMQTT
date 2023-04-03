from paho.mqtt.client import Client
from time import sleep
from random import random, randint
import sys

def on_message(client, userdata, msg):
    try:
        topic = msg.topic
        t = float(msg.payload)
        if topic == 'temperature/t1':
            if t > k1:
                client.subscribe('humidity/#')
            if t < k1:
                client.unsubscribe('humidity/#')
        if topic == 'humidity/#':
            if t > k2:
                client.unsubscribe('humidity/#')
    except ValueError:
        pass
    except Exception as e:
        raise e
def main(broker, k1, k2):
    userdata = [k1, k2]
    client = Client(userdata=userdata)
    client.on_message = on_message

    print(f'Connecting on {broker}')
    client.connect(broker)

    client.subscribe('temperature/t1')

    client.loop_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} broker')
    broker = sys.argv[1]
    k1 = sys.argv[2]
    k2 = sys.argv[3]
    main(broker, k1, k2)
