import os
from kafka import KafkaProducer, KafkaConsumer

KAFKA_BROKER_ADRESS = os.environ.get('KAFKA_BROKER_ADRESS')

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_ADRESS,
        client_id='service1_producer',
    )

    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_BROKER_ADRESS,
        client_id='service1_consumer',
    )
    # consumer.subscribe(list(transport_chanels.keys()))

    # for message in consumer:
        # pass

    import get_market_candles_pb2 as pb
    from time import sleep

    msg = pb.GetMarketCandles()
    msg.basic_message_info.type = 'REST'
    msg.basic_request_info.type = 'sync'
    msg.basic_request_info.use_sandbox = True
    msg.basic_request_info.response_topic = 'test_topic'
    msg.figi = "BBG0013HGFT4"
    msg.from_ = "2020-12-25T10:10:00.131642+03:00"
    msg.to_ = "2020-12-25T10:15:00.131642+03:00"
    msg.interval = "1min"

    while True:
        producer.send('connector.get.market.candles', value=msg.SerializeToString())
        sleep(2)