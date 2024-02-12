from django.contrib import admin
from django.http import HttpRequest

from .admin_mixin import ExportAsCSVmixin
from .models import Product, Order

class OrderInLine(admin.TabularInline):
    model = Product.orders.through


class Queryset:
    pass

@admin.action(description='Archive products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: Queryset):
    queryset.update(archived=True)
@admin.action(description='Unarchive products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: Queryset):
    queryset.update(archived=False)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVmixin):
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv',
    ]
    inlines = [
        OrderInLine,
    ]
    list_display = 'pk', 'name', 'description_short', 'price', 'discount', 'archived'
    list_display_links = 'pk', 'name'
    ordering = 'pk', 'name',
    search_fields = 'name', 'description'
    fieldsets = [
        (None, {
            'fields': ('name', 'description')
        }),
        ('Price options', {
            'fields': ('price', 'discount'),
            'classes': ('collapse', 'wide'),
        }),
        ('Extra Options', {
            'fields': ('archived',),
            'classes': ('collapse',),
            'description': "Extra options. Field 'archived' is for soft delete",
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'
class ProductInLine(admin.StackedInline):
    model = Order.products.through
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]
    list_display = 'delivery_adress', 'promocode', 'created_at', 'user_verbose'
    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')
    def user_verbose(self, obj: Order):
        return obj.user.first_name or obj.user.username


