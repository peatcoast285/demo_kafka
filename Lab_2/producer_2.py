from confluent_kafka import Producer
import random
import time

def produce_messages(producer, topic):
    """ Produce messages to the specified topic """
    for i in range(1, 101):
        message_value = str(i)
        producer.produce(topic, value=message_value.encode('utf-8'))
        print(f'Sent message {i}: {message_value}')
        producer.flush()
        time.sleep(1)

if __name__ == '__main__':
    kafka_broker_url = 'localhost:9092'
    topic_name = 'purchases'
    producer_config = {'bootstrap.servers': kafka_broker_url}
    producer = Producer(producer_config)
    produce_messages(producer, topic_name)
