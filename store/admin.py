from django.contrib import admin
from . models import *

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','product', 'title_g', 'price', 'amount', 'paid', 'order_no', 'payment_date']
admin.site.register(Cart, CartAdmin)