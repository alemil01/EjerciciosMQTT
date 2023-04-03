from paho.mqtt.client import Client
import sys

def on_message(client, userdata, msg):
    try:
        n = msg.payload
        
        #Separamos enteros y reales
        if int(n) == n:
            userdata[0]['Enteros'].append(n)
        else:
            userdata[0]['Reales'].append(n)
            
        #Calculamos la frecuencia de los números que aparecen
        if str(n) in userdata[1].keys():
            userdata[1]['n'] += 1
        else:
            userdata[1]['n'] = 1
    except ValueError:
        pass

def main(broker):
    userdata = [{'Enteros': [], 'Reales': []}, {}]
    client = Client(userdata=userdata)
    client.on_message = on_message

    print(f'Connecting on channel numbers on {broker}')

    client.connect(broker)

    client.subscribe('numbers')
    
    client.loop_forever()

if __name__ == '__main__':
    import sys
    if len(sys.argv)<2:
        print(f'Usage: {sys.argv[0]} broker')
    broker = sys.argv[1]
    main(broker)

    

        
        

        

        
