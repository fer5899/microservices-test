from django.db import models


ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('DENIED', 'Denied'),
    ]

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    units = models.IntegerField()
    status = models.CharField(
        max_length=100,
        choices=ORDER_STATUS_CHOICES,
        default='PENDING',
    )
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date']


    def __str__(self):
        return f"Order {self.id} ({self.status}) - {self.units} units"
