import os
import time
import multiprocessing

from kafka import KafkaProducer, KafkaConsumer

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

    def poll(self, res) -> dict:
        res[0] = self.consumer.poll(timeout_ms=5000, max_records=10, update_offsets=True)
        return res
    
    def send_poll(self, pb: ProtoBufClass) -> dict:
        self.consumer.subscribe(pb.basic_request_info.response_topic) 

        manager = multiprocessing.Manager()
        res = manager.dict()
        th = multiprocessing.Process(target=self.poll, args= (res,))
        th.start()

        time.sleep(0.2)
        self.producer.send(pb.basic_request_info.request_topic, pb.SerializeToString())
        th.join()

        self.consumer.unsubscribe()

        return res[0]
