from confluent_kafka import Consumer, KafkaError

def consume_messages(consumer, topic):
    """ Consume messages from the specified topic """
    consumer.subscribe([topic])
    while True:
        message = consumer.poll(1.0)
        # message_out = message.value().decode('utf-8')
        if message is None:
            continue
        if message.error():
            if message.error().code() == KafkaError._PARTITION_EOF:
                print('Reached end of partition')
            else:
                print('Error while consuming message: {}'.format(message.error()))
        else:
            # print('Received message: {}'.format(message.value().decode('utf-8')))
            print(f'Received message: {message.value().decode("utf-8")}')
            

if __name__ == '__main__':
    # Kafka broker configuration
    bootstrap_servers = 'localhost:9092'
    topic = 'purchases'

    # Create a Kafka consumer
    consumer_config = {'bootstrap.servers': bootstrap_servers, 'group.id': 'my-group'}
    consumer = Consumer(consumer_config)

    # Consume messages from the topic
    consume_messages(consumer, topic)
