# Real-Time Sentiment Analysis and Stream Processing Using Apache Kafka and Spark

This project implements a real-time sentiment analysis pipeline that leverages **Apache Kafka**, **Apache Spark Streaming**, and **PostgreSQL** to classify and process tweet sentiments (positive, neutral, or negative) efficiently and at scale.

## 📌 Project Overview

With the growing need to process large-scale data streams in real time, this system is designed to:
- Ingest tweets from a CSV dataset using Kafka producers.
- Classify sentiments using a Python-based sentiment analysis script.
- Process and aggregate sentiment data in real-time with Spark Streaming.
- Store structured data in PostgreSQL for both real-time and batch mode analysis.

## 📊 Architecture

The system follows an end-to-end data pipeline architecture:
1. **Kafka Producer** reads tweets and sends them to a Kafka topic.
2. **Spark Streaming Job** consumes the tweets, classifies sentiment, and outputs:
   - Live sentiment counts to `sentiment_counts` topic.
   - Processed tweets to `processed_tweets` and `db_inserts` topics.
3. **Kafka Consumers**:
   - Display live sentiment counts on the console.
   - Insert structured data into PostgreSQL for batch processing and querying.

## 🔧 Technologies Used

- **Apache Kafka** – Real-time data ingestion and message brokering.
- **Apache Spark Streaming** – Real-time stream processing and transformations.
- **PostgreSQL** – Persistent storage for historical data analysis.
- **Python** – For producing, consuming, and processing tweets.

## 🛠️ Installation and Setup

1. **Install Dependencies:**
   ```bash
   pip install kafka-python pyspark psycopg2 pandas
