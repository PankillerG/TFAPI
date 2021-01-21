import os
import tinvest

SANDBOX_TOKEN = os.environ.get('TINKOFF_SANDBOX_TOKEN')
TOKEN = os.environ.get('TINKOFF_TOKEN')

class SyncClient:
    # def __init__(self, token='t.Kb4jiOUoLRPUg_RNfgNNyq0ua8T-4PqJzTDE2HMfwkBqt0CMSNro_fw9vkbEe2z_DyvpRtFghGXEI8zKZW14cA', use_sandbox=True):
    def __init__(self, token=SANDBOX_TOKEN, use_sandbox=True):
        # self.client = tinvest.SyncClient(token=token, use_sandbox=use_sandbox)
        self.client = tinvest.SyncClient(token, use_sandbox=use_sandbox)
    
    # def _cast_candles(self, candles):
    #     def _cast_candle(candle):
    #         candle

    def get_market_candles(self, figi, from_, to_, interval):
        candles = self.client.get_market_candles(figi, from_, to_, tinvest.CandleResolution(interval))
        return str(candles)


class AsyncClient:
    def __init__(self, token='', use_sandbox=True):
        # self.client = tinvest.AsyncClient(token=token, use_sandbox=use_sandbox)
        pass