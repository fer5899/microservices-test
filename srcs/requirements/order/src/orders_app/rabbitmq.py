import pika
import json
from django.conf import settings

class RabbitMQConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RabbitMQConnection, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        self.connection_params = pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT
        )
        self.connection = pika.BlockingConnection(self.connection_params)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='order_events', exchange_type='fanout', durable=True)

    def get_channel(self):
        if self.connection.is_closed:
            self._initialize_connection()
        return self.channel

def emit_order_created_event(order_data):
    rabbitmq = RabbitMQConnection()
    channel = rabbitmq.get_channel()

    # Publish message
    message = json.dumps(order_data)
    channel.basic_publish(exchange='order_events', routing_key='', body=message, properties=pika.BasicProperties(
            content_type='application/json',
            content_encoding='utf-8'
        ),)

    # Note: Do not close the connection here, as it is managed by the singleton class
