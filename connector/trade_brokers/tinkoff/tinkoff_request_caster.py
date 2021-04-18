from schemas import (
    ProtoBufClass
)

class RequestCaster():
    def __init__(self):
        pass

    def get_market_candles(self, pb: ProtoBufClass) -> [str, str, str, str]:
        return pb.figi, pb.from_, pb.to_, pb.interval
