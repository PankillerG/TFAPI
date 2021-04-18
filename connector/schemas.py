# from __future__ import annotations
# from enum import Enum
from typing import TypeVar, NewType, Union

import trade_brokers.tinkoff.tinkoff as trade_broker

import get_market_candles_pb2

__all__ = (
    'KafkaMessage',
    'KafkaMessageTopic',
    'KafkaMessageValue'
)

KafkaMessage = TypeVar('KafkaMessage')
KafkaMessageTopic = NewType('KafkaMessageTopic', str)
KafkaMessageValue = NewType('KafkaMessageValue', str)

ProtoBufClass = Union[get_market_candles_pb2.GetMarketCandles]

Candle = TypeVar('Candle')