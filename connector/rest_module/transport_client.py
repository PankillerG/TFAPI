import os
import time
import multiprocessing

import random

from kafka import KafkaProducer, KafkaConsumer
from kafka.structs import TopicPartition

from schemas import (
    KafkaMessage,
    ProtoBufClass
)

class TransportClient:
    service_name: str

    def __init__(self, service_name: str= 'SomeService'):
        self.service_name = service_name
        self.KAFKA_BROKER_ADRESS = os.environ.get('KAFKA_BROKER_ADRESS')
        self.producer = KafkaProducer(
                bootstrap_servers=self.KAFKA_BROKER_ADRESS,
                client_id=service_name+'_producer',
            )
        self.consumer = KafkaConsumer(
                bootstrap_servers=self.KAFKA_BROKER_ADRESS,
                client_id=service_name+'_consumer',
            )

    # # to do like kafka-python
    # def send(self, topic, value):
    #     self.producer.send(topic, value)
    #     return # some status and etc.

    # def subscribe(self, topic) -> None:
    #     self.consumer.subscribe(topic)

    def poll(self):
        pass
    
    def send_poll(self, pb: ProtoBufClass) -> dict:
        topic_partition = TopicPartition(
            pb.basic_request_info.response_topic,
            0
        )
        self.consumer.assign([topic_partition])
        pos = self.consumer.position(topic_partition)
        self.producer.send(pb.basic_request_info.request_topic, pb.SerializeToString())
        self.consumer.seek(topic_partition, pos)
        res = self.consumer.poll(timeout_ms=5000, max_records=10)
        self.consumer.unsubscribe()
        return res
