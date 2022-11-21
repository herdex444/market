from django.db import models
from home.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title_g = models.CharField(max_length=50, null= True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.IntegerField(null=True, blank=True)
    paid = models.BooleanField()
    order_no = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.product.title_r
    
    class Meta:
        db_table = 'cart'
        managed = True
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_nmae = models.CharField(max_length=30)
    paid = models.BooleanField()
    amount = models.IntegerField()
    pay_code = models.CharField(max_length=50)
    shop_code = models.CharField(max_length=50)
    phone = models.CharField(max_length= 50)
    payment_date = models.DateField(auto_now=True)
    admin_date = models.DateField(auto_now=True)
    admin_note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


