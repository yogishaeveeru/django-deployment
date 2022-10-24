from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Student(models.Model):
    BrandName=models.CharField(max_length=200,null=True)
    OriginCountry=models.CharField(max_length=255,null=True)
    class Meta:
        db_table='MobileBrands'
    def __str__(self):
        return str(self.id) +' '+ self.BrandName + " "+self.OriginCountry
# class Order(models.Model):
#     ORDERID=models.IntegerField()
#     ORDERDATE=models.DateField()
#     SHIIPPINGDATE=models.DateField()
#     PRODUCTID=models.IntegerField()
#     QUANTITY=models.IntegerField()
#     COST=models.IntegerField()
#     Discount=models.FloatField()
#     TotalAmountBeforeTax=models.IntegerField()
#     OrdTotal=models.IntegerField()
#     PaymentMethod=models.CharField(max_length=100)
#     CustomerID=models.IntegerField()
#     CustomerName=models.CharField(max_length=255)
#     City=models.CharField(max_length=100)
#     State=models.CharField(max_length=100)
#     Region=models.CharField(max_length=100)
#     class META:
#         db_table='orderdetails'