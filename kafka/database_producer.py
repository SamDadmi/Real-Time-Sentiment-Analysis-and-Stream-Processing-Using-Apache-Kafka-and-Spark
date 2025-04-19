import pandas as pd
import json
import time
from kafka import KafkaProducer

# Kafka Producer Setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Read CSV Data
df = pd.read_csv('Twitter_Data.csv')

for _, row in df.iterrows():
    data = {
        "text": row['clean_text'],
        "label": int(row['category'])  # -1, 0, or 1
    }
    
    # ✅ Send to "raw_tweets" topic ONLY (Spark will handle processing)
    producer.send("raw_tweets", value=data)
    print(f"[Sent to Kafka - raw_tweets] {data}")
    
    # Simulate streaming delay
    time.sleep(1)

print("[INFO] Raw data sent to Kafka.")
