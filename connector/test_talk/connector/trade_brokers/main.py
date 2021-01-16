from trade_brokers.tink import Client
from trade_brokers.settings import Response_channels
import trade_brokers.data_pb2 as pb

TOKEN = '1234'

client = Client(TOKEN, True)

def controller(message, producer):
    r = pb.CandlesRequest()
    r.ParseFromString(message.value)
    topic = message.topic

    response = pb.Candles()
    response.error = 'popochka' 
    response.success = False
    producer.send(Response_channels[topic], value=response)
    if (topic == 'get_candles'):
        try :
            answer = client.get_candles(r.figi, r.from_, r.to_, r.interval)
            producer.send(Response_channels[topic], value=answer)
        except Exception as err:
            response = pb.Candles()
            response.error = str(err) 
            response.success = False
            producer.send(Response_channels[topic], value=response)