# ════════════════════════════════════════════════════════
#  admin.py — Topic 5: لوحة الإدارة
# ════════════════════════════════════════════════════════

from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ('name', 'price')   # أعمدة تظهر في القائمة
    search_fields = ('name',)           # شريط البحث


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ('customer_name', 'phone', 'product', 'quantity', 'status')
    list_filter   = ('status',)         # فلتر جانبي حسب الحالة
    search_fields = ('customer_name', 'phone')
