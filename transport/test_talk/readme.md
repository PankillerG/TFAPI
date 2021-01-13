# Using app

## Install

You simply need to do a QuickStart in trasport directory

## QuickStart

- Start a simple app example (producer and consumer):

```bash
$ docker-compose -f docker-compose.app.yml up
```

- Start a simple app example (producer and consumer) in a background:

```bash
$ docker-compose -f docker-compose.app.yml up
```

## Usage

Show a stream of messages in the topic X (from the transport directory):

(you can optionally add `--from-beginning`)

```bash
$ docker-compose -f docker-compose.kafka.yml exec kafka-broker kafka-console-consumer --bootstrap-server localhost:9092 --topic X
```

Topics:

* get_candles: from requester to server with dict {figi, from_, to, t}
* return_candles: from server to requester with dict {success, err, candles: [{}, ...]}
* test_everything: for testing messages beeing send
* wrong_topic: second topic for server to subdcribe, when message comes there, tries to send to other topic

## Finish

- To stop app use:

```bash
$ docker-compose -f docker-compose.app.yml down
```
