from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List
from json import JSONEncoder
import json

__all__ = (
    'Candle',
    'Candles',
)
class Candle(BaseModel, JSONEncoder):
    c: float
    h: float
    l: float
    o: float
    time: datetime
    v: int

    def toJson(self):
        def inherit(o):
            modified = o.__dict__
            modified['time'] = str(modified['time'])
            return modified
        
        return json.dumps(self, default=inherit)

class Candles(BaseModel):
    candles: List[Candle]