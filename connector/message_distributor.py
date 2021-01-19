import trade_brokers.tinkoff as trade_broker

import get_market_candles_pb2

def message_distributor(message):

    if message.topic == 'connector.get.market.candles':
        pb = get_market_candles_pb2.GetMarketCandles()
        pb.ParseFromString(message.value)
        some_value = trade_broker.get_market_candles(pb.figi, pb.from_, pb.to_, pb.interval)
        return pb.basic_message_info.response_topic, some_value
