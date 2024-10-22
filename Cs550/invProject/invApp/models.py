from django.db import models

# Create your models here.
class Products(models.Model):
               product_id = models.AutoField(primary_key=True)
               product_name = models.CharField(max_length=50)
               sku=models.CharField(max_length=50 ,unique=True)
               price = models.FloatField(default=0)
               quantity=models.IntegerField(default=0)
               supplier=models.CharField(max_length=50)

               def __str__(self):
                       return f"Product: {self.product_name}, SKU: {self.sku}, Price: {self.price}, Quantity: {self.quantity}"
                      