from celery import shared_task
from .models import Order
from .serializers import OrderSerializer

@shared_task(name='receive_order_processed_event')
def receive_order_processed_event(processed_order_data):
    order_id = processed_order_data.get('id')
    if not order_id:
        # Log the error and raise an exception
        raise ValueError("Order ID is required to update an order.")

    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        # Log the error and raise an exception
        raise ValueError(f"Order with ID {order_id} does not exist.")

    serializer = OrderSerializer(order, data=processed_order_data)
    if not serializer.is_valid():
        # Log the error and raise an exception
        raise ValueError(f"Invalid order data: {serializer.errors}")

    serializer.save()
