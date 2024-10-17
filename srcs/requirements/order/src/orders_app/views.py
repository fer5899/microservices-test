from .models import Order
from .serializers import OrderSerializer
from celery import current_app
from django.http import Http404
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics



class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        created_order = serializer.save()
        created_order_data = OrderSerializer(created_order).data
        print(f"Created order: {created_order_data}")
        # emit order created event
        transaction.on_commit(lambda: current_app.send_task(
            'process_order_created_event', 
            args=[created_order_data], 
            queue='order_events',
        ))



class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
