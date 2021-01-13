import os
import json
from random import randint
from time import sleep
from kafka import KafkaProducer

KAFKA_BROKER_ADRES = os.environ.get('KAFKA_BROKER_ADRES')

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_ADRES,
        value_serializer=lambda value: json.dumps(value).encode()
    )

    while True:
        message = 'TEST MSG' + str(randint(1, 10 ))
        producer.send('test_topic', value=message)
        sleep(2)

if __name__ == '__main__':
    main()