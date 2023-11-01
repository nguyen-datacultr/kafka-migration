from kafka import KafkaProducer
import json


producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
    )

topic = "test-topic"
message = b"Hello, Kafka!"
producer.send(topic, value=message)
producer.flush()
producer.close()
