# from __future__ import annotations
# from enum import Enum
from typing import TypeVar, NewType, Union

import get_market_candles_pb2

__all__ = (
    'KafkaMessage',
    'KafkaMessageTopic',
    'KafkaMessageValue'
)

KafkaMessage = TypeVar('KafkaMessage')
KafkaMessageTopic = NewType('KafkaMessageTopic', str)
KafkaMessageValue = NewType('KafkaMessageValue', str)

ProtoBufClass = Union[
    get_market_candles_pb2.GetMarketCandles,
    get_market_candles_pb2.GetMarketCandlesResponse]

Candle = TypeVar('Candle')