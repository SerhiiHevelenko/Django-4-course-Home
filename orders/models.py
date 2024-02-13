from collections.abc import Iterable
from tabnanny import verbose
from django.db import models
from goods.models import Products

from users.models import User
from carts.models import CartQueryset

from django.db.models.signals import post_save
from main.main import disable_for_loaddata

class OrderitemQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="Користувач", default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення замовлення")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефону")
    requires_delivery = models.BooleanField(default=False, verbose_name="Потрібна доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адреса доставки")
    payment_on_get = models.BooleanField(default=False, verbose_name="Оплата під час отримання")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=50, default='Обробляється', verbose_name="Статус замовлення")
    total_price= models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Сума замовлення")

    class Meta:
        db_table = "order"
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
    
    class OrderitemQueryset(models.QuerySet):
        
        def total_price(self):
            return sum(item.products_price() for item in self.items.all())
    
    def __str__(self):
        return f"Замовлення № {self.pk} | Покупець: {self.user.first_name} {self.user.last_name}" 


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Замовлення")
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Продукт", default=None)
    name = models.CharField(max_length=150, verbose_name="Назва")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ціна")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажу")    
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name="Сума замовлення")

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданий товар"
        verbose_name_plural = "Продані товари"

    objects = OrderitemQueryset.as_manager()
   
    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.name} | Замовлення № {self.order.pk}"

    def save(self, *args, **kwargs):
        price = self.product.sell_price()
        self.price = price
        
        self.total_price = int(self.quantity) * price

        super(OrderItem, self).save(*args, **kwargs)


@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = OrderItem.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=OrderItem)