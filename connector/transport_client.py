import os
from kafka import KafkaProducer, KafkaConsumer

from topics import connector_topics
from message_distributor import MessageDistributor

KAFKA_BROKER_ADRESS = os.environ.get('KAFKA_BROKER_ADRESS')

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_ADRESS,
        client_id='connector_producer',
    )

    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_BROKER_ADRESS,
        client_id='connector_consumer',
    )
    consumer.subscribe(connector_topics)

    message_distributor = MessageDistributor()
    for message in consumer:
        message, topic = message_distributor.distribute_message(message)
        producer.send(topic, value=message)