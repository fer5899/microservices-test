from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('stock/', include('stock_app.urls')),
    path('admin/', admin.site.urls),
]
