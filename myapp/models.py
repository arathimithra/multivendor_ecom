from django.db import models
from django.contrib.auth.models import User

#vendor model
class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.username

#product category
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(null=True)

    def __str__(self):
        return self.title

#product model
class Product(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    details = models.TextField(null=True)
    image = models.ImageField(null=True,blank=True)
    price = models.FloatField()



    def __str__(self):
        return self.title
