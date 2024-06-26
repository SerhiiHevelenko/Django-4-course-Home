from django.contrib import admin

from orders.models import Order, OrderItem

# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity", "total_price"
    search_fields = (
        "order",
        "product",
        "name",
    )


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
class OrderAdmin(admin.ModelAdmin):
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
