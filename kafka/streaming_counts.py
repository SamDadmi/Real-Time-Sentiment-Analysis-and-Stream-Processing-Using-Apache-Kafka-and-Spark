from kafka import KafkaConsumer

# Kafka Consumer setup
consumer = KafkaConsumer(
    'sentiment_counts',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='sentiment_debugger',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Listening to 'sentiment_counts'...")

# Hard-coded sentiment order
sentiments = ["positive", "neutral", "negative"]
index = 0  # Start at the first sentiment

for message in consumer:
    # Extract count from the message
    count = message.value

    # Map to the corresponding sentiment label
    sentiment = sentiments[index % len(sentiments)]  # Rotate through sentiments
    print(f"{sentiment.capitalize()}: {count}")

    index += 1  # Move to the next sentiment
