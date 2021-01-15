import os
import json
from time import sleep
from kafka import KafkaConsumer, KafkaProducer
import data_pb2

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
        value_serializer=lambda value: value.SerializeToString()
    )


    consumer = KafkaConsumer(
        'return_candles',
        bootstrap_servers=KAFKA_BROKER_ADRES,
    )

    sleep(50) ## this guy is faster than connector, so we have to wait 

    for f in figis:
        request = data_pb2.CandlesRequest()
        request.figi = f
        request.from_ = "2020-12-25T10:10:00.131642+03:00"
        request.to_ = "2020-12-25T11:00:00.131642+03:00"
        request.interval = "1min"

        producer.send('get_candles', value=request)
    
    counter = 0

    for message in consumer:
        response = data_pb2.Candles()
        response.ParseFromString(message.value)


        notificate = data_pb2.Text()
        notificate.text = 'correct' + str(counter)
        counter += 1
        producer.send('wrong_topic', value=notificate)
    

if __name__ == '__main__':
    main()