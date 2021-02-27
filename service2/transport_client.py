# from rest_module import TransportClient
from rest_module import ConnectorClient
import os
from time import sleep

def main():
    cc = ConnectorClient(use_sandbox=True, service_name='service2')
    res = cc.get_market_candles('BBG0013HGFT4', '2020-12-25T10:10:00.131642+03:00', '2020-12-25T10:15:00.131642+03:00', '1min')
    print(res)
