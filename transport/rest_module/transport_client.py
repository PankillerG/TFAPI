import os
from kafka import KafkaProducer, KafkaConsumer
import time
# import threading
import multiprocessing

class TransportClient:
    def __init__(self, service_name = 'SomeService'):
        self.KAFKA_BROKER_ADRESS = os.environ.get('KAFKA_BROKER_ADRESS')
        
        self.producer = KafkaProducer(
                bootstrap_servers=self.KAFKA_BROKER_ADRESS,
                client_id=service_name+'_producer',
            )

        self.consumer = KafkaConsumer(
                bootstrap_servers=self.KAFKA_BROKER_ADRESS,
                client_id=service_name+'_consumer',
            )
    
    # to do like kafka-python
    def send(self, topic, value):
        self.producer.send(topic, value)
        return # some status and etc.

    def subscribe(self, topic):
        self.consumer.subscribe('test_topic')

    def poll(self, res):
        res[0] = self.consumer.poll(timeout_ms=5000, max_records=10, update_offsets=True)
        # print(res)
        return res
    
    def send_poll(self, topic, value):
        self.consumer.subscribe('test_topic') 

        manager = multiprocessing.Manager()
        res = manager.dict()
        th = multiprocessing.Process(target=self.poll, args= (res,))
        th.start()

        time.sleep(1)
        self.producer.send(topic, value)
        th.join()
        return res
