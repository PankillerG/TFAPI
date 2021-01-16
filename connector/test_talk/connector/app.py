import os
from time import sleep
from kafka import KafkaProducer, KafkaConsumer
import json 
from trade_brokers.main import controller
from trade_brokers.settings import Subscribtions

KAFKA_BROKER_ADRES = os.environ.get('KAFKA_BROKER_ADRES')

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

    consumer.subscribe(Subscribtions)

    sleep(10)
    sleep(10)

    for message in consumer:
        controller(message, producer)

if __name__ == '__main__':
    main()