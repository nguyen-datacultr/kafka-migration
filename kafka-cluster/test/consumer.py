from kafka import KafkaConsumer

# Define Kafka broker(s) and topic
bootstrap_servers = 'localhost:9092'  # Replace with your Kafka broker address
topic = 'test-topic'  # Replace with the name of your Kafka topic

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    bootstrap_servers=[
        "localhost:9092",
    ],
    group_id="python-group",
    auto_offset_reset='earliest',
    )
consumer.subscribe(topics=[topic])
print("Consumer:", consumer)

# Start consuming messages
for message in consumer:
    print("Listening...")
    # Decode the message value (assuming it's in bytes)
    message_value = message.value.decode('utf-8')
    print(f"Received message: {message_value}")
