#!/bin/bash

#KAFKA_BIN=/home/pes2ug22cs094/kafka/bin

#$KAFKA_BIN/kafka-topics.sh --create --topic raw_tweets --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
#$KAFKA_BIN/kafka-topics.sh --create --topic processed_tweets --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
#$KAFKA_BIN/kafka-topics.sh --create --topic db_inserts --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

kafka-topics.sh --create --topic raw_tweets --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic processed_tweets --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic db_inserts --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic sentiment_counts --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
