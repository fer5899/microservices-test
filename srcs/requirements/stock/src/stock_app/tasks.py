from celery import shared_task, current_app
from .models import Box
from .serializers import OrderSerializer
from django.db import transaction

@shared_task(name='process_order_created_event')
def process_order_created_event(order_data):
    # Process the order created event
    serializer = OrderSerializer(data=order_data)
    if not serializer.is_valid():
        # Log the error and raise an exception
        raise ValueError(f"Invalid order data: {serializer.errors}")
    validated_order_data = serializer.validated_data

    boxes = Box.objects.all()
    total_units_in_stock = sum([box.units for box in boxes])
    if validated_order_data.get('units') > total_units_in_stock:
        validated_order_data['status'] = 'DENIED'
    else:
        validated_order_data['status'] = 'ACCEPTED'

    # Emit order processed event
    transaction.on_commit(lambda: current_app.send_task(
        'receive_order_processed_event', 
        args=[validated_order_data], 
        queue='stock_events'
    ))
