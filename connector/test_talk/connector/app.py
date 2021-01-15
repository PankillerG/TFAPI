import os
from time import sleep
from kafka import KafkaProducer, KafkaConsumer
import json 
from clients.tink import Client
import data_pb2

KAFKA_BROKER_ADRES = os.environ.get('KAFKA_BROKER_ADRES')

TOKEN = '1234'

client = Client(TOKEN, True)

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_ADRES, 
        value_serializer=lambda value: value.SerializeToString()
    )
    
    consumer = KafkaConsumer(
        'get_candles',
        bootstrap_servers=KAFKA_BROKER_ADRES,
        value_deserializer=lambda x: x
        
    )
    consumer.subscribe(('get_candles', 'wrong_topic'))

    sleep(10)
    sleep(10)

    for message in consumer:
        r = data_pb2.CandlesRequest()
        r.ParseFromString(message.value)
        answer = ''

        if (message.topic == 'get_candles'):
            try :
                answer = client.get_candles(r.figi, r.from_, r.to_, r.interval)
                producer.send('return_candles', value=answer)
            except Exception as err:
                response = data_pb2.Candles()
                response.error = str(err) 
                response.success = False
                producer.send('return_candles', value=response)

if __name__ == '__main__':
    main()