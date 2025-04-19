import sys
import os
import json


# Make sure utils is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.sentiment import map_label_to_sentiment

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, udf, to_json, struct
from pyspark.sql.types import StructType, StringType, IntegerType

# Initialize Spark session
spark = SparkSession.builder.appName("TweetProcessor").getOrCreate()

# Schema for Kafka data
schema = StructType() \
    .add("text", StringType()) \
    .add("label", IntegerType())

# UDF for sentiment mapping
sentiment_udf = udf(map_label_to_sentiment, StringType())

# ✅ Read from Kafka (raw_tweets topic)
raw_df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "raw_tweets") \
    .load()

# ✅ Parse JSON and process data
parsed_df = raw_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.text", "data.label") \
    .withColumn("sentiment", sentiment_udf(col("label")))

# ✅ 1. Write processed data to Console (for debugging)
parsed_df.writeStream \
    .format("console") \
    .outputMode("append") \
    .start()

# ✅ 2. Write processed data to Kafka (`processed_tweets`)
processed_df = parsed_df.select(to_json(struct("text", "sentiment")).alias("value"))

processed_df.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "processed_tweets") \
    .option("checkpointLocation", "/tmp/kafka-checkpoint-processed") \
    .outputMode("append") \
    .start()

#spark.streams.awaitAnyTermination()

# ✅ 3. Write processed data to Kafka (`db_inserts`)
db_inserts_df = parsed_df.select(to_json(struct("text", "sentiment")).alias("value"))

db_inserts_df.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "db_inserts") \
    .option("checkpointLocation", "/tmp/kafka-checkpoint-dbinserts") \
    .outputMode("append") \
    .start() \
    .awaitTermination()