from pyspark.sql import Row
from pyspark.sql import SparkSession

# PostgreSQL configurations
POSTGRES_URL = "jdbc:postgresql://localhost:5432/tweetdb"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "likh@24#"
POSTGRES_TABLE = "tweets_streamed"

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("PostgreSQLTest") \
    .getOrCreate()

# Test data
test_data = [Row(text="Test tweet", sentiment="positive")]
test_df = spark.createDataFrame(test_data)

# Write to PostgreSQL
test_df.write \
    .format("jdbc") \
    .option("url", POSTGRES_URL) \
    .option("dbtable", POSTGRES_TABLE) \
    .option("user", POSTGRES_USER) \
    .option("password", POSTGRES_PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .mode("append") \
    .save()
