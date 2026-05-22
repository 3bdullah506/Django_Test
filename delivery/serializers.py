# ════════════════════════════════════════════════════════
#  serializers.py — Topic 10: Django REST Framework
#  الـ Serializer يحوّل بيانات قاعدة البيانات إلى JSON
#  وهو عكسي أيضاً: يقبل JSON ويحوّله لكائن Python
# ════════════════════════════════════════════════════════

from rest_framework import serializers
from .models import Product, Order


# Serializer للمنتجات — يحدد أي حقول تظهر في الـ JSON
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Product
        fields = ['id', 'name', 'price']  # id يضاف تلقائياً من Django


# Serializer للطلبات
class OrderSerializer(serializers.ModelSerializer):
    # product_name ← حقل إضافي لعرض اسم المنتج بدلاً من رقمه فقط
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model  = Order
        fields = ['id', 'customer_name', 'phone', 'address',
                  'product', 'product_name', 'quantity', 'status']
