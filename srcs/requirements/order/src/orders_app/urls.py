from django.urls import path
# csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', csrf_exempt(views.OrderList.as_view())),
    path('<int:pk>/', csrf_exempt(views.OrderDetail.as_view())),
]

urlpatterns = format_suffix_patterns(urlpatterns)
