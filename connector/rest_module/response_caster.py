import sys

sys.path.insert(0, '../transport/messages_types_python/')
import get_market_candles_pb2

class ResponseCaster():
    def __init__(self):
        pass

    def get_market_candles(self, response) -> get_market_candles_pb2.GetMarketCandlesResponse:
        pb = get_market_candles_pb2.GetMarketCandlesResponse()
        for partition in response:
            for message in response[partition]:
                pb.ParseFromString(message.value)
                break
        return pb