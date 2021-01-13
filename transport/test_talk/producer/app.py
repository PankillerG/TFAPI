import os
from time import sleep
from kafka import KafkaProducer, KafkaConsumer
import json 
from clients.tink import Client

KAFKA_BROKER_ADRES = os.environ.get('KAFKA_BROKER_ADRES')

TOKEN = '1324'

client = Client(TOKEN, True)

def main():
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_ADRES)
    
    consumer = KafkaConsumer(
        'get_candles',
        bootstrap_servers=KAFKA_BROKER_ADRES,
        value_deserializer=lambda x: json.loads(str(x,'utf-8'))
    )
    consumer.subscribe(('get_candles', 'wrong_topic'))

    sleep(10)
    for message in consumer:
        r = message.value
        answer = ''
        if (message.topic == 'get_candles'):
            try :
                answer = json.dumps(client.get_candles(r['figi'], r['from_'], r['to'], r['t']))
                producer.send('return_candles', value=str(answer).encode())
            except Exception as err:
                producer.send('test_everything', value=str(err).encode())
        else :
            answer = {
                'm': 'AWARE WRONG TOPIC WAS TAKEN!!!',
                'v': message.value,
                't': message.topic,
                'o': message.offset,
                'k': message.key,
                'p': message.partition,
            }
            producer.send('test_everything', value=json.dumps(answer).encode())

if __name__ == '__main__':
    main()