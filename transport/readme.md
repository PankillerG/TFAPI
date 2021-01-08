# Using transport

## Install

You simply need to create a Docker network called kafka-network to enable communication between the Kafka cluster and the apps:

```bash
$ docker network create kafka-network
```

## QuickStart

* Run a simple single Kafka-cluster:

```bash
$ docker-compose -f docker-compose.kafka.yml up
```

* Run a simple single Kafka-cluster in a background:

```bash
$ docker-compose -f docker-compose.kafka.yml up -d
```