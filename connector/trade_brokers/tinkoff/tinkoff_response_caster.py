import get_market_candles_pb2

from typing import TypeVar, List, Union, NewType
from schemas import (
    KafkaMessageValue,
    ProtoBufClass,
    Candle
)

class ResponseCaster():
    def __init__(self):
        pass
    
    def _cast_candles(self, candles: List[Candle]) -> ProtoBufClass:
        def _cast_candle(t_candle):
            candle = get_market_candles_pb2.Candle()
            candle.o = t_candle.o
            candle.c = t_candle.c
            candle.l = t_candle.l
            candle.h = t_candle.h
            candle.time = str(t_candle.time)
            return candle
        
        casted_candles = list(map(_cast_candle, candles))
        pb = get_market_candles_pb2.GetMarketCandlesResponse()
        pb.candles.extend(casted_candles)
        pb.basic_response_info.status = 'OK'
        return pb

    def get_market_candles(self, response) -> KafkaMessageValue:
        candles = response.payload.candles
        pb = self._cast_candles(candles)
        return pb.SerializeToString()