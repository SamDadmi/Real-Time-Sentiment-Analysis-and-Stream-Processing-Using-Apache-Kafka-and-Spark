from kafka import KafkaConsumer
import psycopg2
import json

# PostgreSQL connection setup
try:
    conn = psycopg2.connect(
        dbname="tweetdb",
        user="postgres",
        password="dbt",  # Replace with your PostgreSQL password
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    print("[INFO] Connected to PostgreSQL successfully.")
except Exception as e:
    print(f"[ERROR] Could not connect to PostgreSQL: {e}")
    exit(1)

# Kafka Consumer setup
consumer = KafkaConsumer(
    'db_inserts',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='db_writer',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening to 'db_inserts' (will only receive data if Spark is running)...")

for message in consumer:
    db_data = message.value
    print("[Kafka Consumer] Received from Kafka - DB Inserts:", db_data)

    # Insert into PostgreSQL
    try:
        cursor.execute(
            "INSERT INTO tweets_streamed (text, sentiment) VALUES (%s, %s)",
            (db_data['text'], db_data['sentiment'])
        )
        conn.commit()
        print("[Inserted into PostgreSQL]:", db_data)
    except Exception as e:
        print(f"[ERROR] Failed to insert into PostgreSQL: {e}")

# Close PostgreSQL connection (when terminating the script)
cursor.close()
conn.close()
print("[INFO] PostgreSQL connection closed.")
