# Using app

## Install

You simply need to do a QuickStart in trasport directory

## QuickStart

* Start a simple app example (producer and consumer):

```bash
$ docker-compose -f docker-compose.app.yml up
```

* Start a simple app example (producer and consumer) in a background:

```bash
$ docker-compose -f docker-compose.app.yml up -d
```

## Usage

Show a stream of messages in the topic X (from the transport directory):

(you can optionally add `--from-beginning`)
```bash
$ docker-compose -f docker-compose.kafka.yml exec kafka-broker kafka-console-consumer --bootstrap-server localhost:9092 --topic X
```

Topics:
* test_topic: from producer to consumer
* test_topic2: from cosumer (only for checking)

## Finish

* To stop app use:

```bash
$ docker-compose -f docker-compose.app.yml down
```