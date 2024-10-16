from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('orders/', include('orders_app.urls')),
    path('admin/', admin.site.urls),
]
