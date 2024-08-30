from django.contrib import admin
from .models import Item, Tax, Discount, Order


admin.site.register(Item)
admin.site.register(Tax)
admin.site.register(Discount)
admin.site.register(Order)
