from import_export import resources
from orders.models import Order, OrderItem

class OrderResource(resources.ModelResource):

    class Meta:
        model = Order

class OrderItemResourse(resources.ModelResource):

    class Meta:
        model = OrderItem
