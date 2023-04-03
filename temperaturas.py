from paho.mqtt.client import Client
import sys

def on_message(client, userdata, msg):
    try:
        topic = msg.topic
        t = float(msg.payload)
        if topic in userdata.keys():
            userdata['topic'].append(n)
        else:
            userdata['topic'] = [n]
    except ValueError:
        pass
    except Exception as e:
        raise e

def main(broker):
    userdata = {}
    client = Client(userdata = userdata)
    client.on_message = on_message

    print(f'Connecting on temperature channels on {broker}')
    client.connect(broker)
    client.subscribe('temperature/#')
    client.loop_forever()

    while True:
        temps_total = []
        for topic in userdata.keys():
            temps = []
            for t in userdata['topic']:
                temps.append(t)
            m = media(temps)
            maxim = max(temps)
            minim = min(temps)
            print(f'En {topic}, la temperatura maxima es {maxim}, la minima es {minim} y la  media es {m}')
            temps_total.append(m)
            temps = []
        n = media(temps_total)
        print(f'La temperatura media total es {n}')
        sleep(randon()*8)

def media(lst):
    m = 0
    for i in lst:
        m += i
    media = m/len(lst)
    return media
                
            
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} broker')
    broker = sys.argv[1]
    main(broker)
