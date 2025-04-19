from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'processed_tweets',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='processed_debugger',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening to 'processed_tweets' (will only receive data if Spark is running)...")

for message in consumer:
    print("[Kafka Consumer] Received from Kafka - Processed Tweets:", message.value)
