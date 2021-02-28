import os
from kafka import KafkaProducer, KafkaConsumer
import time
import multiprocessing

class TransportClient:
    def __init__(self, service_name = 'SomeService'):
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

    # to do like kafka-python
    def send(self, topic, value):
        self.producer.send(topic, value)
        return # some status and etc.

    def subscribe(self, topic):
        self.consumer.subscribe(topic)

    def poll(self, res):
        # for message in self.consumer:
        #     res[0] = message
        #     return res
        res[0] = self.consumer.poll(timeout_ms=5000, max_records=10, update_offsets=True)
        # print(res)
        return res
    
    def send_poll(self, topic, value, response_topic):
        self.consumer.subscribe(response_topic) 

        manager = multiprocessing.Manager()
        res = manager.dict()
        th = multiprocessing.Process(target=self.poll, args= (res,))
        th.start()

        time.sleep(1)
        self.producer.send(topic, value)
        th.join()

        return res[0]
