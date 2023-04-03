from paho.mqtt.client import Client
from time import sleep
import pickle
from random import random, randint
import sys


def on_message(client, userdata, msg):
    try:
        mesg = msg.payload #Suponemos que los mensajes son una lista con los parametros
        pickle.dumps(eval(msg))
        time = msg[0]
        topic = msg[1]
        data = msg[2]
        sleep(time)
        client.publish(topic, data)
    except ValueError:
        pass
    except Exception as e:
        raise e

def main(broker):
    client = Client()
    client.on_message = on_message

    print(f'Connecting on timing channels on {broker}')
    client.connect(broker)
    client.subscribe('clients/timing')
    client.loop_forever()


            
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} broker')
    broker = sys.argv[1]
    main(broker)
