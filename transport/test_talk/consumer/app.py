import os
import json
from time import sleep
from kafka import KafkaConsumer, KafkaProducer
KAFKA_BROKER_ADRES = os.environ.get('KAFKA_BROKER_ADRES')

intervals = ['1min', '5min', '1hour', '1day']

figis = [ ## testing examples for each instrument
    'BBG0013HGFT4', ## currencies
    'BBG00KHGQP89', ## bonds
    'BBG000CTQBF3', ## stocks
    'BBG333333333', ## efts
    ]

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_ADRES,
    )


    consumer = KafkaConsumer(
        'return_candles',
        bootstrap_servers=KAFKA_BROKER_ADRES,
        value_deserializer=lambda x: json.loads(str(x,'utf-8'))
    )

    sleep(10)
    for f in figis:
        request = {
            'figi': f,
            'from_': "2020-12-25T10:10:00.131642+03:00",
            'to': "2020-12-25T11:00:00.131642+03:00",
            't': "1min"
        }
        producer.send('get_candles', value=str(json.dumps(request)).encode())
    
    counter = 0
    for message in consumer:
        counter += 1
        producer.send('wrong_topic', value=json.dumps({'msg': 'OK!', 'count': counter}).encode())
    

if __name__ == '__main__':
    main()