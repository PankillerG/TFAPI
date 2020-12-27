import tinvest

client = tinvest.SyncClient(TOKEN, use_sandbox=True)
# tmp = client.get_market_currencies()
# print(tmp)

tmp = client.get_market_candles('BBG0013HGFT4', '2020-12-25T10:10:00.131642+03:00', '2020-12-25T11:00:00.131642+03:00', tinvest.CandleResolution('1min'))

# print(type(tmp))
print(tmp.payload.candles[0])
# print(tmp.payload.candles)