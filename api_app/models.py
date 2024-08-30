'''
Django Модель Item с полями (name, description, price)
Создание модели для заказов (по желанию)
'''

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(default=0.00, verbose_name='Название')
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return f'{self.name} - {self.price}'


# Создание модели для заказов (по желанию)

class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def total_price(self):
        return sum(item.price for item in self.items.all()) - self.discount + self.tax

    def __str__(self):
        return f'Order {self.id}'


class Discount(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name




