import pika
import json
from django.conf import settings

# This can be improved by creating a singleton class to manage the connection to avoid 
# creating a new connection every time we want to emit an event

def emit_order_processed(stock_data):
    # Set up connection parameters
    connection_params = pika.ConnectionParameters(host=settings.RABBITMQ_HOST, port=settings.RABBITMQ_PORT)
    
    # Establish connection to RabbitMQ
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declare the exchange or queue if necessary
    channel.exchange_declare(exchange='stock_events', exchange_type='fanout')

    # Publish message
    message = json.dumps(stock_data)
    channel.basic_publish(exchange='stock_events', routing_key='', body=message)

    # Close the connection
    connection.close()
