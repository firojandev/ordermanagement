from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    type = models.CharField(max_length=1, default='R') # R-Retail/W-WholeSale/B-Both
    address = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, default='A')
    class Meta:
        db_table = 'customers'
