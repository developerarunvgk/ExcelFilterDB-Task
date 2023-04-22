from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255,null=True)
    code = models.CharField(max_length=50,null=True)
    parent_code = models.CharField(null=True,max_length=50, blank=True)
    category_l1 = models.CharField(max_length=255)
    category_l2 = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    enable = models.CharField(max_length=3)
    size=models.CharField(max_length=255)
    UPC=models.CharField(max_length=255)