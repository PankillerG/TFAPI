import tinvest
from schemas import (Candle)

class Client:
    client = {}

    def __init__(self, token, use_sandbox):
        self.client = tinvest.SyncClient(token, use_sandbox=use_sandbox)
    
    def cast_candles(self, candles):
        def cast_candle(x):
            return Candle(c=x.c, h=x.h, l=x.l, o=x.o, time=x.time, v=x.v).toJson()
        
        ##return list(map(cast_candle, candles))
        if len(candles) > 0:
            return {'succes': True, 'candles' : list(map(cast_candle, candles))}
        return {'sucess': False, 'candles': [], 'err': 'no candles available'}


    def get_candles(self, figi, from_, to, interval):
        try:
            candles = self.client.get_market_candles(figi, from_, to, tinvest.CandleResolution(interval))
            return self.cast_candles(candles.payload.candles)
        except Exception as err:
            return {'sucess': False, 'candles': [], 'err': str(err)}