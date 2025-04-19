from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, IntegerType, TimestampType

# Initialize Spark session
spark = SparkSession.builder.appName("KafkaSentimentAggregator").getOrCreate()

# Schema for Kafka data
schema = StructType() \
    .add("text", StringType()) \
    .add("label", IntegerType()) \
    .add("sentiment", StringType())

# Read from Kafka (processed_tweets topic)
processed_df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "processed_tweets") \
    .load()

# Parse JSON and add event-time column (Kafka's timestamp)
parsed_df = processed_df.selectExpr("CAST(value AS STRING)", "timestamp AS event_time") \
    .select(from_json(col("value"), schema).alias("data"), col("event_time")) \
    .select("data.text", "data.sentiment", "event_time")

# Group by sentiment and count tweets
aggregated_df = parsed_df \
    .withWatermark("event_time", "2 minutes") \
    .groupBy("sentiment") \
    .count()

# Write aggregated results to a new Kafka topic (sentiment_counts)
aggregated_df.selectExpr("CAST(sentiment AS STRING) AS key", "CAST(count AS STRING) AS value") \
    .writeStream \
    .outputMode("update") \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "sentiment_counts") \
    .option("checkpointLocation", "/tmp/kafka-checkpoint-sentiment") \
    .start() \
    .awaitTermination()
