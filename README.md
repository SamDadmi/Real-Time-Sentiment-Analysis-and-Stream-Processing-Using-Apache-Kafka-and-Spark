[DBT_VJ_02.pdf](https://github.com/user-attachments/files/19822309/DBT_VJ_02.pdf)
# Real-time Twitter Sentiment Analysis using Apache Kafka, Spark Streaming, and PostgreSQL.

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
- **Python** – For producing, consuming, and processing tweets.![Real-Time Twitter Sentiment Analysis using Apache Kafka, Spark Streaming, and PostgreSQL](https://github.com/user-attachments/assets/6d353f3d-78a7-41ba-b61a-2290cd5d859a)

