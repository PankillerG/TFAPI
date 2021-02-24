import os
import tinvest

import get_market_candles_pb2

SANDBOX_TOKEN = os.environ.get('TINKOFF_SANDBOX_TOKEN')
TOKEN = os.environ.get('TINKOFF_TOKEN')

class SyncClient:
    def __init__(self, token=SANDBOX_TOKEN, use_sandbox=True):
        self.client = tinvest.SyncClient(token, use_sandbox=use_sandbox)
    
    def __cast_candles(self, t_candles):
        def __cast_candle(t_candle):
            candle = get_market_candles_pb2.Candle()
            candle.o = t_candle.o
            candle.c = t_candle.c
            candle.l = t_candle.l
            candle.h = t_candle.h
            candle.time = str(t_candle.time)
            return candle
        
        get_market_candles_response = get_market_candles_pb2.GetMarketCandlesResponse()
        casted_candles = list(map(__cast_candle, t_candles))
        get_market_candles_response.candles.extend(casted_candles)
        get_market_candles_response.basic_response_info.status = 'OK'
        return get_market_candles_response


    def get_market_candles(self, figi, from_, to_, interval):
        response = self.client.get_market_candles(figi, from_, to_, tinvest.CandleResolution(interval))
        t_candles = response.payload.candles
        get_market_candles_response = self.__cast_candles(t_candles)
        return get_market_candles_response.SerializeToString()
        # return str(get_market_candles_response).encode()


class AsyncClient:
    def __init__(self, token='', use_sandbox=True):
        # self.client = tinvest.AsyncClient(token=token, use_sandbox=use_sandbox)
        pass