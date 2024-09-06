from django.contrib import admin
from orders.resources import OrderItemResourse, OrderResource

from orders.models import Order, OrderItem

from import_export.admin import ImportExportModelAdmin

# admin.site.register(Order)
# admin.site.register(OrderItem)



class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0
    

@admin.register(OrderItem)
class OrderItemAdmin(ImportExportModelAdmin):
    list_display = "order", "product", "name", "price", "quantity", "total_price"
    search_fields = (
        "order",
        "product",
        "name",
    )
    resource_class = OrderItemResourse

class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "created_timestamp",
        "total_price",
    )

    search_fields = (
        "user",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "user",
        "created_timestamp",
        "total_price"
    )


    search_fields = (
        "id",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        
        "created_timestamp",
        "user"
    )
    inlines = (OrderItemTabulareAdmin,)

    resource_class = OrderResource