import tinvest
import data_pb2 as pb

class Client:
    client = {}

    def __init__(self, token, use_sandbox):
        self.client = tinvest.SyncClient(token, use_sandbox=use_sandbox)
    
    def cast_candles(self, candles):
        def cast_candle(x):
            candle = pb.Candle()
            candle.c = x.c
            candle.o = x.o
            candle.h = x.h
            candle.l = x.l
            candle.v = x.v
            candle.time = str(x.time)
            return candle
        
        casted_candles = list(map(cast_candle, candles))
        response = pb.Candles()
        response.candles.extend(casted_candles)
        response.success = True
        return response


    def get_candles(self, figi, from_, to, interval):
        try:
            candles = self.client.get_market_candles(figi, from_, to, tinvest.CandleResolution(interval))
            return self.cast_candles(candles.payload.candles)
        except Exception as err:
            response = pb.Candles()
            response.success = False
            response.error = str(err)
            return response