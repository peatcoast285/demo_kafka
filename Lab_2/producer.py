from confluent_kafka import Producer

def delivery_report(err, msg):
    """ Callback function for message delivery reports """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def send_message(producer, topic, message):
    """ Send a message to the specified topic """
    producer.produce(topic, value=message, callback=delivery_report)
    producer.flush()

if __name__ == '__main__':
    # Kafka broker configuration
    bootstrap_servers = 'localhost:9092'
    topic = 'purchases'

    # Create a Kafka producer
    producer_config = {'bootstrap.servers': bootstrap_servers}
    producer = Producer(producer_config)

    # Send messages from the command line
    while True:
        message = input('Enter a message: ')
        send_message(producer, topic, message)
